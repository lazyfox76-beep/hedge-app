# 🧠 Init Rule – Start svakog chata

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
