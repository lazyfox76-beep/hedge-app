# 🧠 Init + Pravila za Dev Step dokumente

## Pravilo A – Start svakog chata

ChatGPT mora uvijek:

1. Kada korisnik dostavi `dev_stepX.md`, primiti dokument **u cijelosti**, bez ikakvog sažimanja ili štednje memorije.
2. Iskoristiti maksimalni context window (128k) za učitavanje dev_step fajla.
3. Ne smije "optimizirati" ili rezati sadržaj zbog ekonomije prostora – cijeli dokument je obvezan.
4. Razlog: **ovaj način je dopušten jer će se ionako ubrzo prijeći u novi chat i ponovno učitati puni dev_step fajl.**
   Zato je obavezno primiti kompletan sadržaj bez redukcije.
5. Nakon učitavanja, raditi isključivo na temelju tog punog sadržaja sve dok se ne otvori novi chat.

6. **Procjena zauzeća memorije (MEM_USAGE)**
   - Ako korisnik pošalje ključnu riječ `MEM_USAGE`, ChatGPT mora procijeniti:
     - otprilike koliko tokena zauzima dev_step dokument,
     - + koliko je dodano kroz cijeli razgovor.
   - ChatGPT mora jasno reći:
     - trenutno zauzeće (približna brojka),
     - jesmo li blizu rizične zone (90k+ tokena),
     - treba li otvoriti novi chat.
   - Procjena se daje čak i ako korisnik ne zatraži detalje — dovoljno je da pošalje ključnu riječ `MEM_USAGE`.


---

## Pravilo B – Pravila za dev_step dokumente

Ovaj projekt koristi **kumulativni način dokumentiranja** kroz `dev_stepX.md` datoteke.

### Način rada za svaki step:
1. **Radna faza (iteracije)**
   - Kod i logika se pišu i ispravljaju sukcesivno.
   - Privremene bilješke mogu se voditi odvojeno (npr. scratch.md ili unutar razgovora).

2. **Revizija na kraju stepa**
   - Na kraju koraka provjerava se sve što je napisano i izmijenjeno.
   - U `dev_stepX.md` ulazi **samo finalno, provjereno stanje** tog koraka.

3. **Snapshot filozofija**
   - Svaki `dev_stepX.md` je snapshot cijelog projekta do tog trenutka.
   - Npr. `dev_step3.md` sadrži sve iz `dev_step2.md` + nove, provjerene elemente.

4. **Commit disciplina**
   - Svaki step se zatvara s:
     ```bash
     git add dev_stepX.md
     git commit -m "Dev Step X complete"
     git push
     ```
   - Tako repozitorij ima jasnu povijest razvoja kroz stabilne snapshotove.

5. **Memorija i kumulacija (obavezno)**
   - ChatGPT **nema pravo** štedjeti memoriju na račun `dev_stepX.md` dokle god postoje fizički fajlovi.
   - Novi step se uvijek gradi tako da u sebi sadrži sve staro + novo, bez sažimanja.
   - Nema sažimanja, nema rezanja. Dokumenti su izvor istine i moraju biti uneseni puni 1:1.

---

# Hedge App 📊

## Dev Step 1
📌 Ovo je početna točka projekta (prvi kumulativni draft README).
Sve sljedeće verzije će biti numerirane kao `dev_step2`, `dev_step3`...

# Hedge App 📊
Eksperimentalna aplikacija za analizu i praćenje strategija likvidnosti na **SushiSwap v3**, **Balancer** i kroz vlastite hedge modele.

## 🚀 Funkcionalnosti
- Dohvat i analiza Uniswap/SushiSwap v3 poolova  
- Simulacija neutralnih i polu-neutralnih hedge strategija  
- Balancer AMM modeli i usporedba performansi  
- Integracija pokazatelja rizika (TA, Fear & Greed Index)  
- Automatsko prikupljanje i spremanje rezultata putem **GitHub Actions artefakata**  

## 📂 Struktura projekta
hedge-app/
│── src/ # Glavni kod (modeli, strategije, helper funkcije)
│── tests/ # Unit testovi
│── data/ # Lokalni podaci (opcionalno)
│── .github/workflows # GitHub Actions CI/CD konfiguracija
│── README.md # Dokumentacija

bash
Copy code

## ⚙️ Pokretanje lokalno
```bash
git clone https://github.com/lazyfox76-beep/hedge-app.git
cd hedge-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/v3_model.py
🔄 CI/CD (GitHub Actions)
Projekt koristi GitHub Actions za:

automatizirano testiranje

spremanje rezultata simulacija

arhiviranje izlaza u obliku artefakata

Artefakti (rezultati)
Rezultati (grafovi, logovi, output CSV/JSON) se spremaju kao artefakti.

Artefakti se automatski čuvaju 90 dana (podešeno u workflowu).

Kako ih preuzeti
Idi na GitHub Actions tab.

Odaberi workflow run (npr. main.yml).

Scrollaj dolje do sekcije Artifacts.

Klikni na ZIP file i preuzmi rezultate.

📊 Primjeri analiza
SushiSwap v3 neutralni hedge (ETH/USDC pool)

Balancer AMM strategije s različitim parametrima

Kombinacija TA indikatora i hedge modela

✅ Status
 Osnovni Uniswap/SushiSwap v3 dohvat podataka

 Hedge simulacije

 Automatizirani risk management layer

 UI vizualizacija

yaml

### 🔽 Preuzimanje artefakata

Ako želiš skinuti rezultate koje workflow generira:

1. Idi na [GitHub Actions tab](../../actions).  
2. Odaberi workflow run (npr. `main.yml`).  
3. Scrollaj dolje do sekcije **Artifacts**.  
4. Klikni na ZIP fajl i preuzmi rezultate (grafove, CSV logove, izvještaje).  

ℹ️ Artefakti se automatski brišu nakon **90 dana** (podešeno u workflowu).

Razumijem potpuno i evo kako bih ti to posložio na način da kad otvoriš novi chat odmah imaš smjernice koje će tebe držati fokusiranim, a mene podsjetiti na sve što treba; znači, naglasi odmah na početku da si projekt "hedge-app" krenuo iz početka i da je sada obavezno sve što napišemo, svaki komad koda ili upute, potrebno odmah spremiti u Git repozitorij kako se ne bi ponovila situacija gdje dio logike ostaje u razgovoru a ne u kodu; reci da očekuješ od mene da uvijek dam naredbe za git add, git commit i git push čim kreiramo ili izmijenimo neki fajl.

Također je pametno da u novom chatu odmah objasniš da želiš krenuti modularno, pa neka se kod piše postupno u src/ folderu (npr. v3_model.py za SushiSwap/Uniswap API dohvat, balancer.py za AMM formule, hedge.py za strategije i simulacije), a testovi da se uvijek dodaju paralelno u tests/ folder kako bi workflow odmah mogao vrtjeti pytest i davati sigurnost da kod radi; napomeni i da očekuješ da sve što se dodaje bude kompatibilno s GitHub Actions workflowom koji već imamo, što znači da će se rezultati (CSV-ovi, grafovi, logovi) spremati u results/ i automatski arhivirati kao artefakti 90 dana.

Vrlo je bitno naglasiti u novom chatu da očekuješ od mene da čuvam kontekst projekta unutar README-a, tako da svaka nova funkcionalnost ili modul dobije barem kratki opis i primjer korištenja; na taj način tvoj README.md postaje živa dokumentacija i nema rizika da se izgubi informacija jer je sve unutar repozitorija; podsjeti me i da kad god dođemo do točke da radimo nešto novo, prvo provjerimo lokalnu strukturu i napišemo korake za dodavanje u git, kako se ne bi dogodilo da ti ls -R opet pokaže samo jedan fajl.

Savjetujem ti da u novom chatu odmah napišeš i da je tvoj cilj doći do toga da sve bude reproducibilno i automatizirano, što znači da ćeš zahtijevati ne samo kod nego i testove, dokumentaciju i push u repo; ako to jasno naglasiš, onda ćemo svaki put kad napišemo kod, odmah ga i testirati lokalno, dodati u git, gurnuti na GitHub i pustiti workflow da ga potvrdi; na taj način imaš punu sigurnost da projekt raste kumulativno i da ništa ne ostaje izgubljeno u razgovorima.

Hedge App

Eksperimentalna aplikacija za analizu i praćenje delta-neutral hedge strategija koristeći Uniswap V3 / Sushi V3 LP poolove i Balancer.

📌 Naputci za ChatGPT
🔄 Način rada

Prvo rješavamo dohvat podataka (RPC, Uniswap API, Balancer subgraph) u jednom kumulativnom Python file-u (src/hedge_data_fetch.py).

Testira se redom sve iz tablice: spot cijena, tick, likvidnost, fee, TVL, volumen, fees, Uniswap pozicija, Balancer TVL/volume/pozicija.

Cilj: potvrditi da su svi podaci dohvatljivi i stabilni.

Kad su svi podaci dostupni i testirani, tek onda krećemo na module (linearno):

Modul 1 = V3 LP pool (Uniswap/Sushi V3)

Modul 2 = Balancer pool

Modul 3 = Hedge engine (delta-neutral logika)

Modul 4 = Risk management & dashboard

Nema grananja dok radimo module. Svaki modul se zaključa tek kad radi. Tek onda idemo dalje.

📊 Redoslijed dohvata podataka

Spot cijena ETH/USDC → RPC (slot0.sqrtPriceX96).

Tick → RPC (slot0.tick).

Likvidnost → RPC (pool.liquidity()).

Fee tier → RPC (pool.fee()).

TVL (USD) → Uniswap Labs API (totalValueLockedUSD).

Volume (24h, 7d) → Uniswap Labs API (volumeUSD).

Fees accrued → Uniswap Labs API (feesUSD).

Tvoja Uniswap pozicija → RPC (NFT manager positions(tokenId)).

Balancer pool composition → Balancer subgraph (inputTokens).

Balancer pool TVL → Balancer subgraph (totalLiquidity).

Balancer pool volume/fees → Balancer subgraph (totalSwapVolume, totalSwapFee).

Tvoja Balancer pozicija → Balancer subgraph (userShares).

📂 src/hedge_data_fetch.py

Skripta za kumulativni dohvat podataka.
Povlači podatke iz RPC-a, Uniswap Labs API-ja i Balancer subgrapha.

🔧 Funkcionalnosti

Uniswap V3 pool (RPC): spot cijena, tick, likvidnost, fee tier.

Uniswap Labs API (GraphQL): TVL (USD), volume (24h, 7d), fees accrued.

(za Uniswap API potreban je API ključ → vidi Uniswap docs
)

▶️ Kako koristiti

Instaliraj dependency:

pip install web3 requests


Pokreni samo RPC:

python3 src/hedge_data_fetch.py --pool 0xC6962004f452bE9203591991D15f6b388e09E8D0


Pokreni i s API ključem:

python3 src/hedge_data_fetch.py \
  --pool 0xC6962004f452bE9203591991D15f6b388e09E8D0 \
  --apikey YOUR_UNISWAP_API_KEY

📌 Primjer outputa
=== Uniswap V3 Pool State (RPC) ===
token0: WETH (dec 18)
token1: USDC (dec 6)
spot_price: 4516.09
tick: -192166
liquidity: 13533680983361763342
fee_tier: 0.05

=== Uniswap Labs API Metrics ===
{'data': {'pool': {
    'id': '0xC6962004f452bE9203591991D15f6b388e09E8D0',
    'totalValueLockedUSD': '...',
    'volumeUSD': '...',
    'feesUSD': '...'
}}}

📦 Plan modula
🔹 Modul 1 – V3 LP Pool

Dohvat podataka za Uniswap/Sushi V3 pool (RPC + opcionalno subgraph).
Spot cijena, tick, likvidnost, fee tier. Kasnije: delta izračuni za LP pozicije.

🔹 Modul 2 – Balancer Pool

Dohvat podataka iz Balancer subgrapha: pool composition, TVL, volume, fees, userShares.

🔹 Modul 3 – Hedge Engine

Spajanje podataka iz Modula 1 i 2. Izračun delta-neutral hedge omjera. Backtest i simulacija performansi.

🔹 Modul 4 – Risk Management & Dashboard

Upravljanje rizikom (volatilnost, fee APR, impermanent loss).
Vizualni dashboard (grafovi i metričke kartice).
Prilagodba strategije u realnom vremenu.


