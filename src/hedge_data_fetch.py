#!/usr/bin/env python3
"""
Uniswap V3 pool data fetcher:
- On-chain (RPC): slot0, tick, liquidity, fee tier, spot price
- Uniswap Labs API: TVL, volume, fees (requires API key)

Usage:
  python3 uniswap_pool.py --pool <POOL_ADDRESS> --rpc <RPC_URL> --apikey <YOUR_UNISWAP_API_KEY>
"""

from web3 import Web3
from decimal import Decimal, getcontext
import requests
import argparse

getcontext().prec = 40

# ABIs
POOL_ABI = [
    {"name": "slot0", "outputs": [
        {"type": "uint160", "name": "sqrtPriceX96"},
        {"type": "int24", "name": "tick"},
        {"type": "uint16", "name": "observationIndex"},
        {"type": "uint16", "name": "observationCardinality"},
        {"type": "uint16", "name": "observationCardinalityNext"},
        {"type": "uint8", "name": "feeProtocol"},
        {"type": "bool", "name": "unlocked"},
    ], "inputs": [], "stateMutability": "view", "type": "function"},
    {"name": "liquidity", "outputs": [{"type": "uint128"}], "inputs": [], "stateMutability": "view", "type": "function"},
    {"name": "fee", "outputs": [{"type": "uint24"}], "inputs": [], "stateMutability": "view", "type": "function"},
    {"name": "token0", "outputs": [{"type": "address"}], "inputs": [], "stateMutability": "view", "type": "function"},
    {"name": "token1", "outputs": [{"type": "address"}], "inputs": [], "stateMutability": "view", "type": "function"},
]

ERC20_ABI = [
    {"name": "decimals", "outputs": [{"type": "uint8"}], "inputs": [], "stateMutability": "view", "type": "function"},
    {"name": "symbol", "outputs": [{"type": "string"}], "inputs": [], "stateMutability": "view", "type": "function"},
]

def get_price_from_sqrtPriceX96(sqrtPriceX96, dec0, dec1):
    sqrt_price = Decimal(sqrtPriceX96)
    denom = Decimal(2) ** 96
    ratio = (sqrt_price / denom) ** 2
    return ratio * (Decimal(10) ** dec0) / (Decimal(10) ** dec1)

def fetch_rpc(pool_addr, rpc_url):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    pool = w3.eth.contract(address=Web3.to_checksum_address(pool_addr), abi=POOL_ABI)

    token0 = w3.eth.contract(address=pool.functions.token0().call(), abi=ERC20_ABI)
    token1 = w3.eth.contract(address=pool.functions.token1().call(), abi=ERC20_ABI)

    dec0, dec1 = token0.functions.decimals().call(), token1.functions.decimals().call()
    sym0, sym1 = token0.functions.symbol().call(), token1.functions.symbol().call()

    slot0 = pool.functions.slot0().call()
    sqrtPriceX96, tick = slot0[0], slot0[1]
    liquidity = pool.functions.liquidity().call()
    fee = pool.functions.fee().call()

    price_token1 = get_price_from_sqrtPriceX96(sqrtPriceX96, dec0, dec1)

    return {
        "token0": f"{sym0} (dec {dec0})",
        "token1": f"{sym1} (dec {dec1})",
        "spot_price": float(price_token1),
        "tick": tick,
        "liquidity": liquidity,
        "fee_tier": fee / 1e4,
    }

def fetch_uniswap_api(pool_addr, api_key):
    url = "https://api.uniswap.org/v1/graphql"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    query = f"""
    {{
      pool(id: "{pool_addr.lower()}") {{
        id
        totalValueLockedUSD
        volumeUSD
        feesUSD
      }}
    }}
    """

    resp = requests.post(url, json={"query": query}, headers=headers, timeout=15)
    return resp.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", "-p", required=True, help="Pool address")
    parser.add_argument("--rpc", default="https://arb1.arbitrum.io/rpc", help="RPC URL (Arbitrum)")
    parser.add_argument("--apikey", default=None, help="Uniswap Labs API key")
    args = parser.parse_args()

    print("=== Uniswap V3 Pool State (RPC) ===")
    rpc_data = fetch_rpc(args.pool, args.rpc)
    for k, v in rpc_data.items():
        print(f"{k}: {v}")

    print("\n=== Uniswap Labs API Metrics ===")
    api_data = fetch_uniswap_api(args.pool, args.apikey)
    print(api_data)

