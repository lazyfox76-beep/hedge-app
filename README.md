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

Hoćeš da ti ja napišem konkretan "template poruke" za novi chat koji možeš samo copy-pasteati i tako me odmah usmjeriti na pravi način rada?



