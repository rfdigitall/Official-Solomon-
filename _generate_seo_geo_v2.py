# -*- coding: utf-8 -*-
"""Unique geo SEO pages for Solomon — no thin template clones."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TODAY = date.today().isoformat()
BASE = "https://solomoncarassistance.it"
TEL, TEL_E = "339 599 8469", "+393395998469"
WA = "https://wa.me/393395998469"
LAT, LON = "45.5784035", "10.2310602"
ADDR = "Via Pietro Tamburini 51, 25136 Brescia (BS)"

# Each page: fully unique copy (title, desc, h1, lead, blocks, faq, related)
PAGES = [
  {
    "slug": "zone-brescia",
    "title": "Zone di intervento Brescia e provincia | Solomon Car Assistance",
    "desc": "Mappa delle zone dove interveniamo: Brescia città, Val Trompia, Franciacorta, Lago di Garda. Soccorso stradale H24, senza autostrade. Tel. 339 599 8469.",
    "h1": "Dove interveniamo a Brescia e in provincia",
    "kws": "zone soccorso stradale Brescia, carro attrezzi provincia Brescia, Val Trompia, Franciacorta, Lago di Garda",
    "placename": "Brescia",
    "lead": "Non copriamo «tutta Italia»: lavoriamo su Brescia e provincia, con priorità su Val Trompia e Franciacorta, più la sponda bresciana del Garda. Qui sotto trovi le pagine dedicate per zona e servizio — utili se cerchi un carro attrezzi vicino a te.",
    "blocks": [
      ("Priorità operative", "Val Trompia (Gardone, Lumezzane, Sarezzo…) e Franciacorta (Rovato, Erbusco, Iseo…) sono le aree dove concentriamo più uscite. Brescia città resta sempre attiva H24."),
      ("Cosa non facciamo", "Non operiamo in autostrada: senza autorizzazione non possiamo intervenire sui tratti autostradali. Su strade urbane e provinciali sì."),
      ("Come scegliere la pagina giusta", "Se sei in panne, chiama subito. Se stai leggendo da PC, apri la pagina della tua zona: findi tempi, FAQ e link diretti al telefono."),
    ],
    "bullets": [
      "Brescia città e quartieri",
      "Val Trompia e comuni limitrofi",
      "Franciacorta e Lago d'Iseo",
      "Desenzano, Sirmione, Salò – sponda bresciana",
      "Chiari, Orzinuovi, Gussago e Bassa",
    ],
    "faq": [
      ("Coprite tutta la provincia di Brescia?", "Sì sulle strade urbane e provinciali. Tempi di arrivo variano: città ~30 min, province dipendono dalla distanza."),
      ("Avete basi in Val Trompia o Franciacorta?", "Partiamo dalla sede a Brescia (Via Tamburini) e ci spostiamo rapidamente verso le valli e la Franciacorta."),
      ("Posso prenotare un trasporto non urgente?", "Sì: chiamaci e organizziamo carico/scarico verso officina o domicilio."),
    ],
  },
  {
    "slug": "soccorso-stradale-brescia",
    "title": "Soccorso stradale Brescia 24/7 | Pronto intervento · 339 599 8469",
    "desc": "Soccorso stradale a Brescia città: panne, batteria, apertura porte, traino. Attivi 24/7. Solomon Car Assistance – chiama 339 599 8469.",
    "h1": "Soccorso stradale a Brescia – pronto intervento H24",
    "kws": "soccorso stradale Brescia, pronto intervento Brescia, auto in panne Brescia, soccorso stradale 24 ore Brescia",
    "placename": "Brescia",
    "lead": "Se l'auto si ferma a Brescia – centro, periferia o zona industriale – serve qualcuno che risponda subito. Solomon Car Assistance fa pronto intervento H24: diagnosi rapida al telefono, arrivo mirato, soluzione sul posto o traino in officina.",
    "blocks": [
      ("Quando chiamarci in città", "Guasto improvviso, batteria scarica sotto casa, chiavi chiuse in auto, foratura in un parcheggio, veicolo che non parte dopo un incidente lieve. Non serve aspettare il mattino: siamo già operativi."),
      ("Tempi medi a Brescia", "In città puntiamo a circa 30 minuti, traffico permettendo. Al telefono ti diciamo subito una stima onesta in base a dove ti trovi."),
      ("Mezzi e cura del veicolo", "Carro attrezzi Iveco con pianale: auto, SUV, moto e anche vetture d'epoca. Carico protetto, senza «tirate» improvvisate."),
    ],
    "bullets": [
      "Numero diretto: 339 599 8469 (anche WhatsApp)",
      "Preventivo chiaro prima di partire, quando possibile",
      "Niente interventi in autostrada",
      "Sede: Via Pietro Tamburini 51, Brescia",
    ],
    "faq": [
      ("Quanto costa il soccorso stradale a Brescia?", "Dipende da tipo di intervento e distanza. Al telefono ti diamo un'indicazione immediata, senza sorprese a fine corsa."),
      ("Venite anche di notte in centro?", "Sì, 24/7 inclusi festivi."),
      ("Fate anche solo avviamento batteria?", "Sì: spesso risolviamo sul posto senza traino."),
    ],
  },
  {
    "slug": "carro-attrezzi-brescia",
    "title": "Carro attrezzi Brescia 24h | Traino auto e moto · Solomon",
    "desc": "Carro attrezzi a Brescia per traino auto, moto e furgoni. Pianale professionale, H24. Chiama Solomon 339 599 8469.",
    "h1": "Carro attrezzi a Brescia – traino professionale H24",
    "kws": "carro attrezzi Brescia, carroattrezzi Brescia, traino auto Brescia, carro attrezzi 24 ore Brescia",
    "placename": "Brescia",
    "lead": "Cerchi un carro attrezzi a Brescia che non ti lasci in attesa? Lavoriamo con pianale ribaltabile: carico sicuro verso officina, carrozzeria o indirizzo che indichi tu – giorno e notte.",
    "blocks": [
      ("Traino, non solo «rimorchio»", "Valutiamo se il veicolo può essere caricato integralmente sul pianale (scelta migliore per automatiche, 4x4 e auto basse) oppure se serve soluzione diversa."),
      ("Destinazioni tipiche", "Officine in città, depositi, domicilio del cliente, ritiro dopo incidente. Ti chiediamo indirizzo di consegna già al telefono per ottimizzare il percorso."),
      ("Perché molti ci chiamano due volte", "Prezzo detto chiaro + rispetto del veicolo. Su auto sportive e d'epoca usiamo protezioni dedicate."),
    ],
    "bullets": [
      "Carro attrezzi Iveco Daily professionale",
      "Moto e scooter con attrezzatura dedicata",
      "Trasporti anche fuori provincia su richiesta",
      "No autostrada (manca autorizzazione)",
    ],
    "faq": [
      ("Il carro attrezzi viene anche il weekend?", "Sì, H24 7/7."),
      ("Potete portare l'auto in un'altra provincia?", "Su richiesta sì: concordiamo distanza e costo prima di partire."),
      ("Servono documenti?", "Patente/libretto aiutano; in emergenza partiamo e regoliamo i dettagli sul posto."),
    ],
  },
  {
    "slug": "soccorso-stradale-val-trompia",
    "title": "Soccorso stradale Val Trompia H24 | Gardone, Lumezzane, Sarezzo",
    "desc": "Soccorso stradale in Val Trompia: Gardone V.T., Lumezzane, Sarezzo, Concesio. Carro attrezzi H24. Solomon 339 599 8469.",
    "h1": "Soccorso stradale in Val Trompia – Gardone, Lumezzane, Sarezzo",
    "kws": "soccorso stradale Val Trompia, carro attrezzi Val Trompia, pronto intervento Gardone Val Trompia, soccorso Lumezzane",
    "placename": "Val Trompia",
    "lead": "La Val Trompia non è «lontana» per noi: è una delle zone prioritarie. Se resti in panne tra Concesio, Gardone Val Trompia, Sarezzo o Lumezzane, chiama: organizziamo l'uscita verso la valle senza farti girare numeri generici.",
    "blocks": [
      ("Perché la valle conta", "Strade di fondovalle, sbalzi di quota, traffico nei turni industriali: in Val Trompia serve un soccorso che conosca i tempi reali, non stime da città."),
      ("Comuni che copriamo di frequente", "Gardone Val Trompia, Lumezzane, Sarezzo, Villa Carcina, Concesio e paesi limitrofi. Invia la posizione WhatsApp e partiamo sul pin GPS."),
      ("Cosa portiamo", "Carro attrezzi, avviamento, apertura porte, rifornimento emergenza. Se serve solo batteria, spesso chiudiamo senza traino."),
    ],
    "bullets": [
      "Priorità dichiarata: Val Trompia",
      "GPS WhatsApp per arrivare al punto esatto",
      "H24 anche in valle",
      "No interventi in autostrada",
    ],
    "faq": [
      ("Quanto impiegate da Brescia alla Val Trompia?", "Dipende dal comune e dal traffico; al telefono ti diamo una stima concreta, non generica."),
      ("Venite a Lumezzane di notte?", "Sì."),
      ("Fate traino verso officine della valle?", "Sì, o verso Brescia se preferisci."),
    ],
  },
  {
    "slug": "carro-attrezzi-val-trompia",
    "title": "Carro attrezzi Val Trompia | Traino Lumezzane e Gardone",
    "desc": "Carro attrezzi in Val Trompia per traino auto e moto. Lumezzane, Gardone, Sarezzo. Solomon H24 – 339 599 8469.",
    "h1": "Carro attrezzi in Val Trompia – traino rapido",
    "kws": "carro attrezzi Val Trompia, carroattrezzi Lumezzane, traino auto Sarezzo, carro attrezzi Gardone Val Trompia",
    "placename": "Val Trompia",
    "lead": "Serve un carro attrezzi in Val Trompia che carichi bene su strade strette e dislivelli? Usiamo pianale professionale e concordiamo subito dove consegnare il veicolo – officina locale o Brescia.",
    "blocks": [
      ("Traini tipici in valle", "Dopo guasto meccanico, incidente lieve, cambio gomme impossibile sul ciglio, furgoni aziendali fermi fuori dai capannoni."),
      ("Carico sicuro", "Pianale ribaltabile: meglio per automatiche e veicoli bassi rispetto al traino «a forca» improvvisato."),
      ("Coordina con l'officina", "Se hai già il meccanico in valle, lo chiamiamo o lo avvisiamo all'arrivo – così non perdi tempo doppio."),
    ],
    "bullets": [
      "Lumezzane · Gardone V.T. · Sarezzo",
      "Moto e scooter ok",
      "Preventivo telefonico prima di partire",
    ],
    "faq": [
      ("Il carro passa nei centri storici stretti?", "Valutiamo accesso al telefono; se serve punto di incontro lo decidiamo subito."),
      ("Pagamento?", "Concordato al telefono / sul posto, trasparente."),
    ],
  },
  {
    "slug": "soccorso-stradale-gardone-valtrompia",
    "title": "Soccorso stradale Gardone Val Trompia | Carro attrezzi H24",
    "desc": "Auto in panne a Gardone Val Trompia? Soccorso stradale e carro attrezzi H24. Solomon 339 599 8469.",
    "h1": "Soccorso stradale a Gardone Val Trompia",
    "kws": "soccorso stradale Gardone Val Trompia, carro attrezzi Gardone Valtrompia, pronto intervento Gardone VT",
    "placename": "Gardone Val Trompia",
    "lead": "A Gardone Val Trompia interveniamo per panne, batteria e traino. Non sei un «numero generico Brescia»: diciamo tempi verso Gardone e partiamo con mezzo adatto.",
    "blocks": [
      ("Uscite su Gardone", "Zona residenziale, artigianale e viabilità di valle: chiediamo via e civico o pin WhatsApp per non sbagliare ingresso."),
      ("Se sei sulla SP", "Fermati in sicurezza, accendi le quattro frecce, chiamaci: ti guidiamo su cosa fare mentre arriviamo."),
    ],
    "bullets": ["H24", "Traino o ripartenza sul posto", "Collegato alla rete Val Trompia"],
    "faq": [
      ("Siete di Gardone?", "Siamo basati a Brescia ma la Val Trompia è zona prioritaria di intervento."),
      ("WhatsApp attivo?", "Sì, stesso numero 339 599 8469."),
    ],
  },
  {
    "slug": "soccorso-stradale-lumezzane",
    "title": "Soccorso stradale Lumezzane | Pronto intervento carro attrezzi",
    "desc": "Soccorso stradale a Lumezzane H24: panne, traino, batteria. Solomon Car Assistance 339 599 8469.",
    "h1": "Soccorso stradale a Lumezzane – intervento H24",
    "kws": "soccorso stradale Lumezzane, carro attrezzi Lumezzane, auto in panne Lumezzane",
    "placename": "Lumezzane",
    "lead": "Lumezzane ha traffico e dislivelli: se l'auto non parte in via, cortile o zona produttiva, chiama Solomon. Organizziamo soccorso stradale o carro attrezzi senza passarti da call center.",
    "blocks": [
      ("Punto di ritrovo", "Se il civico è difficile, ci diamo un riferimento chiaro (rotonda, capannone, parcheggio) e arriviamo lì."),
      ("Aziende e furgoni", "Interveniamo anche su veicoli commerciali leggeri fermi fuori sede."),
    ],
    "bullets": ["Diretto in Val Trompia", "Preventivo telefonico", "No autostrada"],
    "faq": [
      ("Trainate furgoni?", "Veicoli commerciali leggeri sì, nei limiti del mezzo."),
      ("Di domenica?", "Sì, H24."),
    ],
  },
  {
    "slug": "soccorso-stradale-sarezzo",
    "title": "Soccorso stradale Sarezzo | Carro attrezzi Val Trompia",
    "desc": "Soccorso stradale a Sarezzo H24. Panne e traino con carro attrezzi. Chiama 339 599 8469.",
    "h1": "Soccorso stradale a Sarezzo",
    "kws": "soccorso stradale Sarezzo, carro attrezzi Sarezzo, pronto intervento Sarezzo Brescia",
    "placename": "Sarezzo",
    "lead": "A Sarezzo rispondiamo per emergenze stradali e traino verso officina. Stessa qualità del servizio Brescia, con attenzione ai tempi verso la media Val Trompia – non un call center lontano.",
    "blocks": [
      ("Cosa fare subito", "Mettiti in sicurezza, chiama il 339 599 8469, invita la posizione se puoi. Partiamo con le info già in mano."),
      ("Verso officina o casa", "Se hai già il meccanico a Sarezzo o verso Gardone, lo indichi al telefono e ottimizziamo il percorso del carro."),
      ("Differenza rispetto a Brescia città", "In valle contano i dislivelli e il traffico dei turni: per questo chiediamo subito il punto esatto (via o pin)."),
    ],
    "bullets": ["H24 Val Trompia", "GPS WhatsApp", "Traino o ripartenza sul posto", "No autostrada"],
    "faq": [
      ("Coprite anche Villa Carcina?", "Sì, area Val Trompia."),
      ("Di notte a Sarezzo?", "Sì, stesso numero H24."),
    ],
  },
  {
    "slug": "soccorso-stradale-franciacorta",
    "title": "Soccorso stradale Franciacorta | Rovato, Erbusco, Iseo H24",
    "desc": "Soccorso stradale in Franciacorta: Rovato, Erbusco, Iseo, Adro. Carro attrezzi H24. Solomon 339 599 8469.",
    "h1": "Soccorso stradale in Franciacorta – Rovato, Erbusco, Iseo",
    "kws": "soccorso stradale Franciacorta, carro attrezzi Franciacorta, soccorso stradale Rovato, pronto intervento Erbusco",
    "placename": "Franciacorta",
    "lead": "Franciacorta è la seconda priorità insieme alla Val Trompia. Tra cantine, SP e paesi (Rovato, Erbusco, Coccaglio, Adro, Iseo) interiamo per panne e traino H24 – senza confondere con servizi autostradali.",
    "blocks": [
      ("Turismo e residenti", "Interveniamo per residenti e per chi è di passaggio: basta una chiamata e il punto GPS."),
      ("Verso Iseo o Brescia", "Consegniamo dove ti è utile: officina in Franciacorta o rientro verso Brescia."),
      ("Strade provinciali", "Lavoriamo su viabilità ordinaria. Autostrade: no."),
    ],
    "bullets": [
      "Rovato · Erbusco · Iseo · Adro · Coccaglio",
      "Priorità operativa Franciacorta",
      "Carro attrezzi + servizi sul posto",
    ],
    "faq": [
      ("Venite la sera dopo una cena in Franciacorta?", "Sì, H24."),
      ("Fate recupero moto?", "Sì."),
      ("Quanto prima mi dite il prezzo?", "Subito al telefono, in base al tipo di intervento."),
    ],
  },
  {
    "slug": "carro-attrezzi-franciacorta",
    "title": "Carro attrezzi Franciacorta | Traino Rovato e Iseo",
    "desc": "Carro attrezzi in Franciacorta per traino auto. Rovato, Erbusco, Iseo. Solomon H24 – 339 599 8469.",
    "h1": "Carro attrezzi in Franciacorta",
    "kws": "carro attrezzi Franciacorta, carroattrezzi Rovato, traino auto Iseo, carro attrezzi Erbusco",
    "placename": "Franciacorta",
    "lead": "Serve trainare l'auto in Franciacorta senza aspettare ore? Carro attrezzi con pianale, contatto diretto, destinazione concordata (officina locale o altrove).",
    "blocks": [
      ("Quando serve il pianale", "Cambio automatico, danni alla ruota, veicolo basso, auto d'epoca: meglio il carico completo."),
      ("Eventi e weekend", "Nei weekend la zona si anima: restiamo comunque raggiungibili al cellulare."),
    ],
    "bullets": ["Traino H24", "Preventivo chiaro", "Zona prioritaria"],
    "faq": [("Portate l'auto a Brescia dalla Franciacorta?", "Sì, su accordo telefonico.")],
  },
  {
    "slug": "soccorso-stradale-rovato",
    "title": "Soccorso stradale Rovato | Carro attrezzi Franciacorta",
    "desc": "Soccorso stradale a Rovato H24. Panne, batteria, traino. Solomon 339 599 8469.",
    "h1": "Soccorso stradale a Rovato",
    "kws": "soccorso stradale Rovato, carro attrezzi Rovato, pronto intervento Rovato BS",
    "placename": "Rovato",
    "lead": "A Rovato interveniamo per emergenze auto: non passare da centrali anonime. Parli con chi organizza l'uscita verso Franciacorta e ti dice subito se conviene ripartenza o traino.",
    "blocks": [
      ("Punto GPS", "Cortili e zone produttive: mandaci la posizione WhatsApp e riduciamo i giri a vuoto."),
      ("Rovato come snodo", "Da qui si raggiunge bene Erbusco, Coccaglio e la dorsale Franciacorta: utile se l'officina non è nello stesso comune."),
      ("Orari", "H24 inclusi weekend: se la panne arriva dopo cena, chiama comunque."),
    ],
    "bullets": ["H24 Franciacorta", "Traino o ripartenza", "Preventivo telefonico", "No autostrada"],
    "faq": [
      ("Siete vicini a Coccaglio?", "Sì, stessa area di intervento."),
      ("Fate apertura porte a Rovato?", "Sì, quando il modello lo consente in sicurezza."),
    ],
  },
  {
    "slug": "soccorso-stradale-iseo",
    "title": "Soccorso stradale Iseo | Lago d'Iseo e Franciacorta",
    "desc": "Soccorso stradale a Iseo e Lago d'Iseo. Carro attrezzi H24. Chiama 339 599 8469.",
    "h1": "Soccorso stradale a Iseo (Lago d'Iseo)",
    "kws": "soccorso stradale Iseo, carro attrezzi Iseo, soccorso stradale Lago d'Iseo",
    "placename": "Iseo",
    "lead": "Ad Iseo e lungo il lago servono tempi chiari e un mezzo adatto. Solomon fa soccorso e traino H24 collegati alla copertura Franciacorta, non un servizio «generico lago».",
    "blocks": [
      ("Lago e paese", "Se sei in lungolago o in collina, dicci il riferimento: organizziamo l'approccio migliore per non bloccare il traffico."),
      ("Stagione e weekend", "Con più movimento turistico i tempi cambiano: meglio chiamare subito e fissare il punto GPS."),
      ("Destinazioni traino", "Officine a Iseo / Franciacorta oppure rientro verso Brescia."),
    ],
    "bullets": ["H24", "Traino verso officina", "GPS WhatsApp", "No autostrada"],
    "faq": [
      ("Coprite anche Sulzano?", "Valutiamo al telefono in base a distanza e disponibilità."),
      ("Intervenite per moto?", "Sì, con attrezzatura dedicata."),
    ],
  },
  {
    "slug": "soccorso-stradale-lago-di-garda",
    "title": "Soccorso stradale Lago di Garda (BS) | Desenzano Sirmione Salò",
    "desc": "Soccorso stradale sponda bresciana del Garda: Desenzano, Sirmione, Salò, Gardone Riviera. H24. 339 599 8469.",
    "h1": "Soccorso stradale sul Lago di Garda – sponda bresciana",
    "kws": "soccorso stradale Lago di Garda, carro attrezzi Desenzano, soccorso stradale Sirmione, carro attrezzi Salò",
    "placename": "Lago di Garda",
    "lead": "Sulla sponda bresciana del Garda (Desenzano, Sirmione, Salò, Gardone Riviera) interveniamo per panne e traino. Idealmente chiama appena ti fermi: traffico stagionale può allungare i tempi, meglio partire subito.",
    "blocks": [
      ("Estate e traffico", "In alta stagione i tempi cambiano: al telefono ti diciamo stime reali, non promesse impossibili."),
      ("Turisti", "Se non conosci la zona, manda il pin WhatsApp: arriviamo al punto senza cercarti a caso."),
      ("Limite importante", "Niente autostrada: solo viabilità ordinaria verso/da il lago."),
    ],
    "bullets": ["Desenzano · Sirmione · Salò · Gardone Riviera", "H24", "Carro attrezzi + servizi sul posto"],
    "faq": [
      ("Venite anche a Peschiera?", "Peschiera è VR: valutiamo solo se fattibile; priorità è sponda BS."),
      ("Serve il carro per un camper?", "Dipende da peso/ingombro: chiedilo subito al telefono."),
    ],
  },
  {
    "slug": "soccorso-stradale-desenzano",
    "title": "Soccorso stradale Desenzano del Garda H24 | Carro attrezzi",
    "desc": "Soccorso stradale a Desenzano del Garda: panne e traino H24. Solomon 339 599 8469.",
    "h1": "Soccorso stradale a Desenzano del Garda",
    "kws": "soccorso stradale Desenzano, carro attrezzi Desenzano del Garda, auto in panne Desenzano",
    "placename": "Desenzano del Garda",
    "lead": "A Desenzano del Garda il soccorso deve arrivare sapendo dove sei (porto, stazione, residenziale, SP). Chiama Solomon: organizziamo pronto intervento o carro attrezzi H24.",
    "blocks": [
      ("Riferimenti utili", "Vicino al lago i civici a volte confondono: meglio GPS o un landmark (parcheggio, rotonda, hotel)."),
      ("Traino post-panne", "Portiamo verso officina a Desenzano o verso Brescia, come preferisci."),
    ],
    "bullets": ["H24", "Sponda bresciana Garda", "Preventivo telefonico"],
    "faq": [
      ("Siete a Desenzano?", "Partiamo da Brescia con copertura Garda BS; tempi comunicati al momento."),
      ("WhatsApp?", "Sì."),
    ],
  },
  {
    "slug": "carro-attrezzi-desenzano",
    "title": "Carro attrezzi Desenzano del Garda | Traino auto H24",
    "desc": "Carro attrezzi a Desenzano del Garda per traino auto e moto. Solomon 339 599 8469.",
    "h1": "Carro attrezzi a Desenzano del Garda",
    "kws": "carro attrezzi Desenzano, carroattrezzi Desenzano del Garda, traino auto Desenzano",
    "placename": "Desenzano del Garda",
    "lead": "Carro attrezzi su Desenzano: carico su pianale e consegna dove indichi. Ideale se l'auto non è più marciante dopo guasto o foratura in zona lago.",
    "blocks": [
      ("Accesso e carico", "Se il punto è stretto, fissiamo un punto di incontro sicuro a pochi metri – meglio di forzare manovre rischiose."),
      ("Estate", "Con più traffico conviene chiamare appena ti fermi: il mezzo parte con destinazione già chiara."),
      ("Moto e auto basse", "Pianale più adatto di soluzioni di fortuna; per sportive chiediamo altezza e assetto al telefono."),
    ],
    "bullets": ["Pianale professionale", "H24", "Moto ok", "No autostrada"],
    "faq": [
      ("Portate l'auto a Sirmione da Desenzano?", "Sì, se richiesto."),
      ("Quanto costa il traino locale?", "Te lo diciamo al telefono in base a distanza e tipo veicolo."),
    ],
  },
  {
    "slug": "soccorso-stradale-sirmione",
    "title": "Soccorso stradale Sirmione | Pronto intervento Lago di Garda",
    "desc": "Soccorso stradale a Sirmione H24. Panne e carro attrezzi. Chiama 339 599 8469.",
    "h1": "Soccorso stradale a Sirmione",
    "kws": "soccorso stradale Sirmione, carro attrezzi Sirmione, auto in panne Sirmione",
    "placename": "Sirmione",
    "lead": "A Sirmione viabilità e afflusso turistico cambiano tutto. Se sei in panne, chiama subito: ti chiediamo punto preciso (penisola, parcheggi, hotel) e organizziamo l'intervento.",
    "blocks": [
      ("Accesso penisola", "In certi orari l'accesso è critico: decidiamo insieme il punto migliore per il mezzo."),
    ],
    "bullets": ["H24", "GPS essenziale", "Traino o ripartenza"],
    "faq": [("Venite nel centro storico?", "Se l'accesso mezzo non è possibile, ci incontriamo nel punto carribile più vicino.")],
  },
  {
    "slug": "soccorso-stradale-salo",
    "title": "Soccorso stradale Salò | Carro attrezzi Alto Garda BS",
    "desc": "Soccorso stradale a Salò H24. Traino e pronto intervento. Solomon 339 599 8469.",
    "h1": "Soccorso stradale a Salò",
    "kws": "soccorso stradale Salò, carro attrezzi Salò, pronto intervento Salò Garda",
    "placename": "Salò",
    "lead": "Su Salò e tratto alto lago bresciano interveniamo per panne e traino. Tempi dipendono da traffico e distanza: te li diciamo onesti al telefono, senza promesse da brochure.",
    "blocks": [
      ("Gardone Riviera e dintorni", "Se sei poco dopo Salò, segnalalo: ottimizziamo l'uscita unica invece di due corse."),
      ("Lungolago e parcheggi", "In estate i punti di sosta cambiano: pin WhatsApp o nome hotel/parcheggio evitano ritardi."),
      ("Cosa risolviamo sul posto", "Batteria, apertura porte, rifornimento emergenza; se non riparte, carico su carro attrezzi."),
    ],
    "bullets": ["H24 sponda BS", "Traino verso officina locale o Brescia", "No autostrada"],
    "faq": [
      ("Fate rifornimento di emergenza?", "Sì, quando ha senso rispetto al traino."),
      ("Venite anche a Maderno?", "Valutiamo al telefono in base alla distanza."),
    ],
  },
  {
    "slug": "soccorso-stradale-chiari",
    "title": "Soccorso stradale Chiari | Carro attrezzi Bassa Bresciana",
    "desc": "Soccorso stradale a Chiari H24. Panne e traino. Solomon 339 599 8469.",
    "h1": "Soccorso stradale a Chiari",
    "kws": "soccorso stradale Chiari, carro attrezzi Chiari, pronto intervento Chiari BS",
    "placename": "Chiari",
    "lead": "A Chiari e nella Bassa bresciana organizziamo soccorso e carro attrezzi. Contatto diretto, senza passaggi inutili: dici dove sei e che problema hai.",
    "blocks": [
      ("Zona Bassa", "Strade ampie e capannoni: spesso le stime sono più lineari rispetto alle valli, ma il traffico dei turni conta comunque."),
      ("Aziende e furgoni", "Se un mezzo aziendale è fermo fuori sede, chiediamo destinazione di riconsegna già al primo contatto."),
      ("Differenza con il Garda", "Qui non c'è il picco turistico del lago, ma restiamo H24 come sul resto della provincia."),
    ],
    "bullets": ["H24", "Traino officina", "Preventivo telefonico", "No autostrada"],
    "faq": [
      ("Coprite Orzinuovi da Chiari?", "Sì, stessa fascia operativa."),
      ("Serve il carro o basta l'avviamento?", "Lo capiamo al telefono e sul posto: non forziamo un traino inutile."),
    ],
  },
  {
    "slug": "soccorso-stradale-orzinuovi",
    "title": "Soccorso stradale Orzinuovi | Pronto intervento BS",
    "desc": "Soccorso stradale a Orzinuovi H24. Carro attrezzi e panne. 339 599 8469.",
    "h1": "Soccorso stradale a Orzinuovi",
    "kws": "soccorso stradale Orzinuovi, carro attrezzi Orzinuovi",
    "placename": "Orzinuovi",
    "lead": "Se sei fermo a Orzinuovi, chiama Solomon: usciamo per ripartenza sul posto o traino verso officina. Numero diretto, senza centralino a più livelli.",
    "blocks": [
      ("Info utili all'appello", "Via + civico o pin WhatsApp. Ti confermiamo stima arrivo subito, in base a dove siamo e al traffico."),
      ("Tipiche chiamate", "Batteria al mattino, foratura fuori paese, veicolo che non parte dal parcheggio del supermercato."),
      ("Destinazione traino", "Officina a Orzinuovi, Chiari o rientro verso Brescia – la scegli tu."),
    ],
    "bullets": ["H24", "Bassa Bresciana", "Preventivo chiaro", "No autostrada"],
    "faq": [
      ("Anche di notte?", "Sì."),
      ("WhatsApp attivo?", "Sì, 339 599 8469."),
    ],
  },
  {
    "slug": "soccorso-stradale-gussago",
    "title": "Soccorso stradale Gussago | Carro attrezzi vicino Brescia",
    "desc": "Soccorso stradale a Gussago H24. Panne e traino rapido verso Brescia. 339 599 8469.",
    "h1": "Soccorso stradale a Gussago",
    "kws": "soccorso stradale Gussago, carro attrezzi Gussago, pronto intervento Gussago",
    "placename": "Gussago",
    "lead": "Gussago è a ridosso di Brescia: spesso i tempi sono più contenuti rispetto alle valli. Ideale per panne notturne o traino veloce in officina cittadina.",
    "blocks": [
      ("Perché conviene chiamare subito", "Sei vicino alla base operativa: più aspetti, più rischi di complicare un guasto semplice."),
      ("Residenziale e artigianale", "Cortili e zone miste: pin WhatsApp o citofono chiaro ci fanno arrivare al posto giusto al primo passaggio."),
      ("Confrontato con Val Trompia", "Meno dislivello, più vicinanza a Brescia – ma restiamo H24 come sul resto della provincia."),
    ],
    "bullets": ["Vicino Brescia", "H24", "GPS WhatsApp", "No autostrada"],
    "faq": [
      ("Venite anche a Cellatica?", "Sì, area limitrofa."),
      ("Solo traino o anche batteria?", "Entrambe, in base al problema."),
    ],
  },
  {
    "slug": "recupero-auto-epoca-brescia",
    "title": "Recupero auto d'epoca Brescia | Trasporto auto classiche",
    "desc": "Recupero e trasporto auto d'epoca e sportive a Brescia. Pianale protetto. Solomon 339 599 8469.",
    "h1": "Recupero auto d'epoca e sportive a Brescia",
    "kws": "recupero auto epoca Brescia, trasporto auto classiche Brescia, carro attrezzi Ferrari Porsche Brescia",
    "placename": "Brescia",
    "lead": "Auto classiche e sportive non si «tirano» come un utilitaria. Solomon carica su pianale con protezioni: collezioni, Mille Miglia spirit, sportive moderne ferme per guasto.",
    "blocks": [
      ("Cura del veicolo", "Cinghie, appoggi, attenzione a spoiler e sottoscocca. Meglio perdere 5 minuti in più che graffiare."),
      ("Trasferimenti", "Da domicilio a officina specializzata, o tra province su accordo."),
    ],
    "bullets": ["Pianale dedicato", "Esperienza auto di valore", "Preventivo dedicato"],
    "faq": [
      ("Trasportate Ferrari/Porsche?", "Sì, con approccio da collezione."),
      ("Solo emergenza o anche programmato?", "Entrambe."),
    ],
  },
  {
    "slug": "batteria-auto-scarica-brescia",
    "title": "Batteria auto scarica Brescia | Avviamento e sostituzione",
    "desc": "Batteria scarica a Brescia? Avviamento sul posto o sostituzione. H24. 339 599 8469.",
    "h1": "Batteria auto scarica a Brescia – partiamo noi",
    "kws": "batteria scarica Brescia, avviamento auto Brescia, sostituzione batteria sul posto Brescia",
    "placename": "Brescia",
    "lead": "Spie spente, click-click in avviamento, auto ferma al supermercato: spesso non serve il carro. Veniamo per avviamento o valutazione batteria sul posto a Brescia e provincia.",
    "blocks": [
      ("Prima il tentativo sul posto", "Se riparte, ti evitiamo un traino inutile. Se la batteria è morta, valutiamo sostituzione o traino breve."),
      ("Inverno e elettronica", "Auto moderne sono sensibili: non improvvisare pinze a caso se non sei pratico – meglio un intervento ordinato."),
    ],
    "bullets": ["H24", "Spesso senza traino", "Anche Val Trompia / Franciacorta"],
    "faq": [
      ("Quanto dura un avviamento?", "Di solito pochi minuti sul posto, se l'impianto risponde."),
      ("Vendete batterie?", "Valutazione sul posto; ti diciamo le opzioni."),
    ],
  },
  {
    "slug": "apertura-porte-auto-brescia",
    "title": "Apertura porte auto Brescia | Chiavi chiuse in macchina",
    "desc": "Chiavi chiuse in auto a Brescia? Apertura porte senza danni. H24. 339 599 8469.",
    "h1": "Apertura porte auto a Brescia – senza danni",
    "kws": "apertura porte auto Brescia, chiavi chiuse in auto Brescia, apertura auto Brescia",
    "placename": "Brescia",
    "lead": "Chiavi in macchina e sportelli bloccati: interveniamo per apertura professionale, con attenzione a cornici e serrature. Meglio non forzare con cacciaviti.",
    "blocks": [
      ("Metodo", "Tecniche non distruttive quando possibile. Se il modello è critico, te lo diciamo prima."),
      ("Dove", "Brescia città e provincia (valli, Franciacorta, Garda BS)."),
    ],
    "bullets": ["H24", "Senza danni quando fattibile", "Stesso numero WhatsApp"],
    "faq": [
      ("Aprite anche auto nuove con keyless?", "Dipende dal modello: al telefono capiamo subito se possiamo intervenire."),
      ("Serve denunciare?", "Solo in casi particolari (furto); per dimenticanza di solito no."),
    ],
  },
]


def related_links(current: str) -> list[tuple[str, str]]:
    out = []
    for p in PAGES:
        if p["slug"] == current:
            continue
        # diversify: prefer different area
        out.append((p["slug"], p["h1"].split("–")[0].split("-")[0].strip()[:60]))
        if len(out) >= 6:
            break
    # always include hub if not hub
    if current != "zone-brescia":
        out = [("zone-brescia", "Tutte le zone Brescia")] + out[:5]
    return out


def split_h1(h1: str) -> tuple[str, str]:
    for sep in (" – ", " - ", " — "):
        if sep in h1:
            a, b = h1.split(sep, 1)
            return a.strip(), b.strip()
    words = h1.split()
    if len(words) <= 4:
        return h1, "Pronto intervento H24"
    mid = max(3, len(words) // 2)
    return " ".join(words[:mid]), " ".join(words[mid:])


def short_lead(lead: str) -> str:
    """Una sola frase corta in hero (il resto va nel body)."""
    for sep in (". ", "! ", "? "):
        if sep in lead:
            return lead.split(sep, 1)[0].strip() + sep.strip()
    return lead if len(lead) < 120 else lead[:117].rsplit(" ", 1)[0] + "…"


def render(p: dict) -> str:
    from urllib.parse import quote

    url = f"{BASE}/{p['slug']}.html"
    line1, line2 = split_h1(p["h1"])
    hero_lead = short_lead(p["lead"])
    blocks_html = ""
    for h, t in p["blocks"]:
        blocks_html += (
            f'      <div class="seo-block">\n'
            f"        <h2>{h}</h2>\n"
            f"        <p>{t}</p>\n"
            f"      </div>\n"
        )
    # lead completo sotto hero (in hero resta solo 1 frase)
    lead_block = (
        f'      <div class="seo-block">\n'
        f"        <p>{p['lead']}</p>\n"
        f"      </div>\n"
    )
    bullets = "\n".join(
        f'        <li><i class="fas fa-check" aria-hidden="true"></i><span>{b}</span></li>'
        for b in p["bullets"]
    )
    faq_html = ""
    faq_json = []
    for q, a in p["faq"]:
        faq_html += (
            f'        <details class="faq-item">\n'
            f"          <summary>{q}</summary>\n"
            f"          <p>{a}</p>\n"
            f"        </details>\n"
        )
        faq_json.append(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        )
    rel = related_links(p["slug"])
    rel_html = "\n".join(f'          <li><a href="/{s}.html">{lab}</a></li>' for s, lab in rel)
    wa = f"{WA}?text={quote('Ciao Solomon, sono in panne a ' + p['placename'] + '. Potete intervenire?')}"

    ld_service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": p["h1"],
        "description": p["desc"],
        "url": url,
        "provider": {
            "@type": "AutomotiveBusiness",
            "@id": f"{BASE}/#organization",
            "name": "Solomon Car Assistance",
            "telephone": TEL_E,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Via Pietro Tamburini 51",
                "addressLocality": "Brescia",
                "postalCode": "25136",
                "addressRegion": "BS",
                "addressCountry": "IT",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
        },
        "areaServed": {"@type": "Place", "name": p["placename"]},
    }
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_json}
    ld_crumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Zone", "item": f"{BASE}/zone-brescia.html"},
            {"@type": "ListItem", "position": 3, "name": p["placename"], "item": url},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <meta name="theme-color" content="#ffb400"/>
  <meta name="format-detection" content="telephone=yes"/>
  <title>{p['title']}</title>
  <meta name="description" content="{p['desc']}"/>
  <meta name="keywords" content="{p['kws']}"/>
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large"/>
  <link rel="canonical" href="{url}"/>
  <link rel="alternate" hreflang="it" href="{url}"/>
  <meta name="geo.region" content="IT-BS"/>
  <meta name="geo.placename" content="{p['placename']}, Lombardia"/>
  <meta name="geo.position" content="{LAT};{LON}"/>
  <meta name="ICBM" content="{LAT}, {LON}"/>
  <meta property="og:type" content="website"/>
  <meta property="og:title" content="{p['title']}"/>
  <meta property="og:description" content="{p['desc']}"/>
  <meta property="og:url" content="{url}"/>
  <meta property="og:image" content="{BASE}/img_p911targa.webp"/>
  <meta property="og:locale" content="it_IT"/>
  <meta property="og:site_name" content="Solomon Car Assistance"/>
  <link rel="icon" type="image/png" href="/favicon-192.png?v=2"/>
  <link rel="preload" as="image" href="/carro-attrezzi-solomon-brescia-flotta-iveco-640.jpg" imagesrcset="/carro-attrezzi-solomon-brescia-flotta-iveco-640.jpg 640w, /carro-attrezzi-solomon-brescia-flotta-iveco.jpg 1024w" imagesizes="100vw"/>
  <link rel="stylesheet" href="/style.css?v=20261009seo"/>
  <link rel="stylesheet" href="/seo-pages.css?v=20261009fix"/>
  <script type="application/ld+json">{json.dumps(ld_service, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(ld_crumb, ensure_ascii=False)}</script>
</head>
<body class="seo-page">
<header class="header" id="header" role="banner">
  <div class="container header-inner">
    <a href="/" class="header-logo" aria-label="Solomon Car Assistance – Home">
      <img src="/logo.jpeg" alt="Solomon Car Assistance" class="logo-img" width="54" height="54"/>
      <span class="logo-text"><span class="logo-name">SOLOMON</span><span class="logo-sub">CAR ASSISTANCE</span></span>
    </a>
    <nav class="nav" id="nav" aria-label="Menu">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/soccorso-stradale-brescia.html">Brescia</a></li>
        <li><a href="/soccorso-stradale-val-trompia.html">Val Trompia</a></li>
        <li><a href="/soccorso-stradale-franciacorta.html">Franciacorta</a></li>
        <li><a href="/zone-brescia.html">Zone</a></li>
      </ul>
    </nav>
    <a href="tel:{TEL_E}" class="header-phone" aria-label="Chiama ora {TEL}">
      <i class="fas fa-phone-alt" aria-hidden="true"></i>
      <span class="phone-text">{TEL}</span>
    </a>
    <button class="hamburger" id="hamburger" aria-label="Apri menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>

<section class="hero" id="home" aria-label="Pronto intervento">
  <div class="hero-bg" aria-hidden="true">
    <div class="hero-bg-media">
      <img
        class="hero-bg-img"
        src="/carro-attrezzi-solomon-brescia-flotta-iveco-640.jpg"
        srcset="/carro-attrezzi-solomon-brescia-flotta-iveco-640.jpg 640w, /carro-attrezzi-solomon-brescia-flotta-iveco.jpg 1024w"
        sizes="100vw"
        alt=""
        width="1024" height="768"
        fetchpriority="high"
      />
    </div>
    <div class="hero-bg-mask"></div>
  </div>
  <div class="hero-grid">
    <div class="hero-top">
      <span class="hero-badge"><span class="hero-badge-dot"></span> Pronto intervento · {p['placename']} 24/7</span>
    </div>
    <div class="hero-bottom">
      <h1>
        <span class="hero-line1">{line1}</span>
        <span class="hero-line2">{line2}</span>
      </h1>
      <p class="hero-desc">{hero_lead}</p>
      <div class="hero-btns">
        <a href="tel:{TEL_E}" class="btn-hero-primary"><i class="fas fa-phone-alt" aria-hidden="true"></i> Chiama ora – {TEL}</a>
        <a href="{wa}" class="btn-hero-wa" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<main>
  <div class="seo-main">
    <div class="container">
      <nav class="seo-crumb" aria-label="Percorso"><a href="/">Home</a> · <a href="/zone-brescia.html">Zone</a> · {p['placename']}</nav>
{lead_block}{blocks_html}
      <div class="seo-block">
        <h2>In sintesi</h2>
        <ul class="seo-points">
{bullets}
        </ul>
      </div>
    </div>
  </div>

  <div class="seo-band">
    <div class="container">
      <h2>Sei in panne a {p['placename']}?</h2>
      <p>Rispondiamo noi. 24/7.</p>
      <div class="hero-btns">
        <a href="tel:{TEL_E}" class="btn-hero-primary"><i class="fas fa-phone-alt" aria-hidden="true"></i> {TEL}</a>
        <a href="{wa}" class="btn-hero-wa" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
      </div>
    </div>
  </div>

  <div class="seo-faq-wrap">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Domande frequenti</span>
        <h2>Domande frequenti</h2>
      </div>
      <div class="faq-grid">
{faq_html}      </div>
    </div>
  </div>

  <div class="seo-more">
    <div class="container">
      <h2>Altre zone</h2>
      <ul>
{rel_html}
      </ul>
      <p class="seo-addr">Sede: {ADDR}</p>
    </div>
  </div>
</main>

<footer class="footer" role="contentinfo">
  <div class="container footer-inner">
    <div class="footer-brand">
      <div class="footer-logo-wrap">
        <img src="/logo.jpeg" alt="Solomon Car Assistance" class="footer-logo" width="44" height="44" loading="lazy"/>
        <span class="footer-logo-text"><span class="logo-name">SOLOMON</span><span class="logo-sub">CAR ASSISTANCE</span></span>
      </div>
      <p>Soccorso stradale e carro attrezzi a <strong>Brescia</strong> e provincia — <strong>24/7</strong>.</p>
    </div>
    <div class="footer-contact">
      <h4>Contatti</h4>
      <a href="tel:{TEL_E}" class="footer-phone"><i class="fas fa-phone-alt" aria-hidden="true"></i> {TEL}</a>
      <a href="{wa}" class="footer-wa" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
      <p><i class="fas fa-map-marker-alt" aria-hidden="true"></i> {ADDR}</p>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p>&copy; 2026 Solomon Car Assistance — P.IVA IT04659930988 — REA BS-631269</p>
      <p class="footer-credit">Realizzato da <a href="https://rfdigital.it" target="_blank" rel="noopener noreferrer">RF Digital</a></p>
    </div>
  </div>
</footer>

<a href="tel:{TEL_E}" class="floating-wa floating-call" aria-label="Chiama Solomon Car Assistance">
  <i class="fas fa-phone-alt" aria-hidden="true"></i><span class="floating-wa-label">Chiama</span>
</a>
<script src="/script.js?v=2606292642" defer></script>
</body>
</html>
"""


def write_sitemap(slugs: list[str]) -> None:
    parts = [
        f"  <url>\n    <loc>{BASE}/</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>"
    ]
    for s in slugs:
        pr = "0.9" if any(x in s for x in ("brescia", "val-trompia", "franciacorta", "desenzano")) else "0.8"
        parts.append(
            f"  <url>\n    <loc>{BASE}/{s}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(parts)
        + "\n</urlset>\n",
        encoding="utf-8",
    )


def main() -> None:
    slugs = []
    for p in PAGES:
        (ROOT / f"{p['slug']}.html").write_text(render(p), encoding="utf-8")
        slugs.append(p["slug"])
        print("unique", p["slug"], "chars", len(p["lead"]) + sum(len(b[1]) for b in p["blocks"]))
    write_sitemap(slugs)
    print("DONE", len(slugs))


if __name__ == "__main__":
    main()
