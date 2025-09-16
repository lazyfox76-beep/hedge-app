# Hedge App
Eksperimentalna aplikacija za analizu i praćenje **DeFi hedge strategija**.  
Podržani protokoli i alati: **Uniswap v3 / SushiSwap v3 liquidity poolovi**, **Balancer AMM modeli**, te integracija sa indikatorima kao što su **Fear & Greed Index** i **TA signali**.  

---

## 🚀 Značajke

- **Delta-neutral LP strategije**  
  - simulacija i testiranje neutralnih pozicija  
  - hedge putem perp short/long parova  
  - analitika PnL i kolaterala

- **AMM modeli (Balancer, Uni/Sushi v3)**  
  - proračuni cijene, likvidnosti i fee-ova  
  - analiza impermanent loss-a  
  - hedging logika i formule

- **Risk Management modul**  
  - integracija s tehničkom analizom (TA)  
  - povezivanje sa sentiment indeksima (Fear & Greed)  
  - dinamičko podešavanje hedge omjera

- **GitHub Actions CI/CD**  
  - automatsko testiranje i build  
  - spremanje artefakata (grafovi, CSV logovi, izvještaji) na **90 dana**  

---

## 📂 Struktura projekta

hedge-app/
├── data/ # primjer CSV datasetova
├── notebooks/ # Jupyter bilježnice za analize
├── src/ # glavni Python moduli
│ ├── amm/ # AMM logika (Uniswap v3, Balancer)
│ ├── hedge/ # Hedge strategije i simulacije
│ └── utils/ # pomoćne funkcije
├── tests/ # unit testovi
├── requirements.txt # Python ovisnosti
├── README.md # ovaj dokument
└── .github/
└── workflows/
└── main.yml # CI/CD workflow

yaml
Copy code

---

## ⚙️ Instalacija

1. Kloniraj repozitorij:

```bash
git clone https://github.com/lazyfox76-beep/hedge-app.git
cd hedge-app
Instaliraj ovisnosti:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
▶️ Pokretanje
Primjer simulacije hedge strategije:

bash
Copy code
python src/hedge/run_strategy.py --pool USDC/ETH --range 1500-2500 --hedge short
🧪 Testiranje
bash
Copy code
pytest tests/
📊 Artefakti (CI/CD)
Svi rezultati (grafovi, izvještaji, logovi) se automatski spremaju putem
GitHub Actions → Artifacts i čuvaju 90 dana.

🔮 Roadmap
 Dodati dashboard za vizualizaciju strategija

 Integracija s on-chain podacima (The Graph)

 Napredni risk management modul

 Machine learning modeli za predikciju volatilnosti

📜 Licenca
MIT License. Slobodno koristi, mijenjaj i eksperimentiraj.

yaml
Copy code

---

👆 Ovo je **"master" README** koji dokumentira projekt od A do Ž.  
Hoćeš da ga odmah prilagodim tako da se u **Artifacts** sekciji eksplicitno naglasi kako korisnik može preuzeti rezultate sa GitHub Actions (korak-po-korak)?
