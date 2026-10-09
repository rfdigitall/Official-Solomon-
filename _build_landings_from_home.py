# -*- coding: utf-8 -*-
"""
Landings SEO/geo = CLONE della homepage (stesso design/CSS/sezioni).
Cambia solo testi, città, zone, FAQ, interventi — zero CSS nuovo.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
BASE = "https://solomoncarassistance.it"
TEL = "339 599 8469"
TEL_E = "+393395998469"
TODAY = date.today().isoformat()

# Ogni pagina: copy UNICA (non clone thin)
PAGES = [
  {
    "slug": "soccorso-stradale-brescia",
    "title": "Soccorso Stradale Brescia 24/7 | Pronto Intervento · Solomon",
    "desc": "Soccorso stradale a Brescia città H24: panne, batteria, apertura porte, traino. Solomon Car Assistance – 339 599 8469.",
    "kws": "soccorso stradale Brescia, pronto intervento Brescia, auto in panne Brescia, soccorso stradale 24 ore",
    "place": "Brescia",
    "badge": "Pronto intervento · Brescia 24/7",
    "h1a": "Soccorso stradale",
    "h1b": "a Brescia H24",
    "hero": "Auto ferma in centro, periferia o zona industriale? Arriviamo in circa 30 minuti. Chiama 339 599 8469.",
    "servizi_intro": "Interventi tipici a Brescia città — dal guasto sotto casa al traino in officina.",
    "servizi": [
      ("Pronto Intervento", "Guasto improvviso a Brescia: rispondiamo subito, giorno e notte."),
      ("Carro Attrezzi", "Traino verso l'officina che scegli tu, con pianale Iveco."),
      ("Recupero Moto", "Moto e scooter caricati con attrezzatura dedicata."),
      ("Batteria Scarica", "Avviamento sul posto in cortile, parcheggio o strada."),
      ("Apertura Porte", "Chiavi chiuse in auto: apertura senza danni quando possibile."),
      ("Rifornimento", "Rimasto a secco in città? Portiamo carburante da te."),
    ],
    "steps_intro": "Tre passi, anche se sei fermo a Brescia di notte.",
    "step3_title": "Arriviamo in ~30 min",
    "step3_p": "In città puntiamo a circa mezz'ora, traffico permettendo. Te lo diciamo già al telefono.",
    "perche": [
      "Arrivo medio <strong>30 minuti</strong> in Brescia città",
      "Attivi <strong>24/7</strong> anche festivi",
      "Pianale professionale per auto, SUV e moto",
      "Preventivo chiaro al telefono",
      "Sede a Via Tamburini 51, Brescia",
      "Niente interventi in autostrada",
    ],
    "zone_h": "Brescia e dintorni",
    "zone_p": "Priorità città; usciamo anche verso Val Trompia, Franciacorta e Garda BS.",
    "zones": [
      ("Brescia Città", "Centro, quartieri, zone produttive.", ["Centro", "Periferia", "Zone industriali"], True),
      ("Val Trompia", "Gardone, Lumezzane, Sarezzo — zona prioritaria.", ["Gardone V.T.", "Lumezzane", "Sarezzo"], False),
      ("Franciacorta & Garda", "Rovato, Iseo, Desenzano, Sirmione.", ["Rovato", "Desenzano", "Sirmione"], False),
    ],
    "faq": [
      ("Quanto impiegate ad arrivare a Brescia città?", "Di solito circa 30 minuti, dipende dal traffico e dal punto esatto."),
      ("Fate solo traino o anche ripartenza sul posto?", "Spesso risolviamo sul posto (batteria, avviamento). Se serve traino, usiamo il carro."),
      ("Venite di notte in centro storico?", "Sì, H24. Se l'accesso è stretto, concordiamo un punto di carico."),
      ("Operete in autostrada?", "No: senza autorizzazione non interveniamo sui tratti autostradali."),
      ("Qual è il numero diretto?", "339 599 8469 — anche WhatsApp."),
      ("Dove siete di sede?", "Via Pietro Tamburini 51, 25136 Brescia."),
    ],
    "cta": ("Sei in panne a Brescia?", "Chiama ora — rispondiamo noi."),
    "nap": "Soccorso Stradale Brescia",
  },
  {
    "slug": "carro-attrezzi-brescia",
    "title": "Carro Attrezzi Brescia 24h | Traino Auto e Moto · Solomon",
    "desc": "Carro attrezzi a Brescia per traino auto, moto e furgoni. Pianale Iveco H24. Chiama 339 599 8469.",
    "kws": "carro attrezzi Brescia, carroattrezzi Brescia, traino auto Brescia, carro attrezzi 24 ore",
    "place": "Brescia",
    "badge": "Carro attrezzi · Brescia 24/7",
    "h1a": "Carro attrezzi",
    "h1b": "Brescia H24",
    "hero": "Serve un carro attrezzi a Brescia che carichi bene e porti dove dici tu? Pianale professionale, preventivo al telefono.",
    "servizi_intro": "Traino e carico a Brescia — destinazione officina, carrozzeria o domicilio.",
    "servizi": [
      ("Traino pianale", "Carico integrale: ideale per automatiche, auto basse e sportive."),
      ("Destinazione a scelta", "Officina, deposito o indirizzo che indichi tu."),
      ("Moto e scooter", "Attrezzatura dedicata, senza rischi al telaio."),
      ("Fuori orario", "Anche di notte e nei festivi."),
      ("Auto d'epoca", "Protezioni anti-graffio su veicoli di valore."),
      ("Preventivo chiaro", "Costo indicato prima di partire, quando possibile."),
    ],
    "steps_intro": "Dal primo contatto al carico sul pianale.",
    "step3_title": "Carichiamo e partiamo",
    "step3_p": "Fissiamo il veicolo sul pianale e lo portiamo dove serve — senza «tirate» improvvisate.",
    "perche": [
      "Pianale Iveco professionale",
      "Esperienza con sportive e classiche",
      "Brescia città e provincia",
      "H24 senza call center",
      "Prezzo detto chiaro",
      "No autostrada",
    ],
    "zone_h": "Dove portiamo i veicoli",
    "zone_p": "Partenza da Brescia; consegne in città, valle e Franciacorta.",
    "zones": [
      ("Officine Brescia", "Consegne frequenti in officine e carrozzerie cittadine.", ["Centro", "Nord", "Sud"], True),
      ("Val Trompia", "Traino verso meccanici di valle o ritorno in città.", ["Gardone", "Lumezzane", "Sarezzo"], False),
      ("Garda BS", "Desenzano e sponda bresciana su richiesta.", ["Desenzano", "Sirmione", "Salò"], False),
    ],
    "faq": [
      ("Il carro viene anche il weekend?", "Sì, H24 7/7."),
      ("Potete portare l'auto fuori provincia?", "Su accordo sì: distanza e costo prima di partire."),
      ("Meglio pianale o forca?", "Per molte auto il pianale è più sicuro: lo scegliamo quando possibile."),
      ("Servono documenti?", "Patente/libretto aiutano; in emergenza regoliamo sul posto."),
      ("Numero carro attrezzi Brescia?", "339 599 8469."),
      ("Trasportate furgoni?", "Veicoli commerciali leggeri nei limiti del mezzo."),
    ],
    "cta": ("Ti serve il carro attrezzi?", "Un numero, risposta diretta."),
    "nap": "Carro Attrezzi Brescia",
  },
  {
    "slug": "soccorso-stradale-val-trompia",
    "title": "Soccorso Stradale Val Trompia | Gardone, Lumezzane, Sarezzo H24",
    "desc": "Soccorso stradale in Val Trompia H24: Gardone V.T., Lumezzane, Sarezzo, Concesio. Solomon 339 599 8469.",
    "kws": "soccorso stradale Val Trompia, carro attrezzi Val Trompia, pronto intervento Gardone, soccorso Lumezzane",
    "place": "Val Trompia",
    "badge": "Priorità · Val Trompia 24/7",
    "h1a": "Soccorso in",
    "h1b": "Val Trompia",
    "hero": "Gardone, Lumezzane, Sarezzo, Concesio: la valle è zona prioritaria. Mandaci il pin WhatsApp e partiamo.",
    "servizi_intro": "Uscite tipiche in Val Trompia — fondovalle, dislivelli, turni industriali.",
    "servizi": [
      ("Pronto Intervento", "Panne sulla SP o fuori dai capannoni: risposta diretta, non call center."),
      ("Carro Attrezzi", "Traino verso officina di valle o Brescia."),
      ("Recupero Moto", "Moto ferme in salita o parcheggio: carico dedicato."),
      ("Batteria", "Avviamento sul posto anche di notte in valle."),
      ("Apertura Porte", "Chiavi in auto a Lumezzane o Gardone: interveniamo."),
      ("Rifornimento", "A secco fuori turno? Portiamo carburante."),
    ],
    "steps_intro": "In valle conta il punto esatto: via, civico o pin.",
    "step3_title": "Arrivo in valle",
    "step3_p": "Tempi variabili per comune e traffico: al telefono ti diamo una stima reale, non generica.",
    "perche": [
      "Val Trompia = <strong>priorità</strong> dichiarata",
      "Conosciamo tempi e viabilità di valle",
      "H24 anche a Lumezzane e Gardone",
      "GPS WhatsApp per non sbagliare ingresso",
      "Traino o ripartenza sul posto",
      "No autostrada",
    ],
    "zone_h": "Comuni Val Trompia",
    "zone_p": "Interveniamo lungo la valle e collegamenti verso Brescia.",
    "zones": [
      ("Gardone V.T.", "Residenziale e artigianale — pin o citofono chiaro.", ["Gardone", "Villa Carcina"], True),
      ("Lumezzane", "Dislivelli e zone produttive: punto di ritrovo se serve.", ["Lumezzane", "Capannoni"], False),
      ("Sarezzo · Concesio", "Media valle e ingresso da Brescia.", ["Sarezzo", "Concesio"], False),
    ],
    "faq": [
      ("Quanto da Brescia a Lumezzane?", "Dipende dall'ora: ti diciamo una stima concreta al telefono."),
      ("Venite di notte in Val Trompia?", "Sì, stesso numero H24."),
      ("Trainate verso officine della valle?", "Sì, o verso Brescia se preferisci."),
      ("Passate nei centri stretti?", "Valutiamo accesso; se serve punto di incontro lo decidiamo subito."),
      ("Numero per la valle?", "339 599 8469."),
      ("Fate autostrada?", "No."),
    ],
    "cta": ("Fermo in Val Trompia?", "Scrivi o chiama — partiamo verso la valle."),
    "nap": "Soccorso Stradale Val Trompia",
  },
  {
    "slug": "carro-attrezzi-val-trompia",
    "title": "Carro Attrezzi Val Trompia | Traino Lumezzane e Gardone",
    "desc": "Carro attrezzi in Val Trompia: traino auto e moto a Lumezzane, Gardone, Sarezzo. H24 · 339 599 8469.",
    "kws": "carro attrezzi Val Trompia, carroattrezzi Lumezzane, traino Gardone Val Trompia",
    "place": "Val Trompia",
    "badge": "Carro attrezzi · Val Trompia",
    "h1a": "Carro attrezzi",
    "h1b": "Val Trompia",
    "hero": "Traino in valle con pianale: carico sicuro su strade di fondovalle e dislivelli. Concordiamo subito dove consegnare.",
    "servizi_intro": "Traini tipici tra i comuni della Val Trompia.",
    "servizi": [
      ("Traino valle", "Dopo guasto, incidente lieve o foratura sul ciglio."),
      ("Pianale", "Meglio del traino improvvisato su automatiche e auto basse."),
      ("Officina locale", "Se hai già il meccanico in valle, ottimizziamo il percorso."),
      ("Moto", "Carico dedicato anche in salita."),
      ("Aziende", "Furgoni leggeri fermi fuori sede."),
      ("Notte", "H24 su richiesta urgente."),
    ],
    "steps_intro": "Dimmi dove sei e dove deve arrivare il veicolo.",
    "step3_title": "Consegna in valle o Brescia",
    "step3_p": "Portiamo dove serve: officina di valle o rientro in città.",
    "perche": [
      "Focus Val Trompia",
      "Pianale professionale",
      "Coordiniamo con la tua officina",
      "Preventivo telefonico",
      "H24",
      "No autostrada",
    ],
    "zone_h": "Percorsi frequenti",
    "zone_p": "Lumezzane ↔ Gardone ↔ Sarezzo ↔ Brescia.",
    "zones": [
      ("Lumezzane", "Uscite frequenti zona produttiva.", ["Lumezzane"], True),
      ("Gardone V.T.", "Residenziale e artigianale.", ["Gardone"], False),
      ("Verso Brescia", "Traino in officina cittadina su richiesta.", ["Concesio", "Brescia"], False),
    ],
    "faq": [
      ("Il carro passa nei vicoli stretti?", "Valutiamo al telefono; organizziamo punto di carico."),
      ("Pagamento?", "Concordato al telefono / sul posto."),
      ("Solo emergenza?", "Anche trasporti programmati."),
      ("Numero?", "339 599 8469."),
      ("Moto ok?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Serve il carro in Val Trompia?", "Chiamaci e partiamo."),
    "nap": "Carro Attrezzi Val Trompia",
  },
  {
    "slug": "soccorso-stradale-franciacorta",
    "title": "Soccorso Stradale Franciacorta | Rovato, Erbusco, Iseo H24",
    "desc": "Soccorso stradale in Franciacorta H24: Rovato, Erbusco, Iseo, Adro. Solomon 339 599 8469.",
    "kws": "soccorso stradale Franciacorta, carro attrezzi Franciacorta, pronto intervento Rovato, soccorso Iseo",
    "place": "Franciacorta",
    "badge": "Priorità · Franciacorta 24/7",
    "h1a": "Soccorso",
    "h1b": "Franciacorta",
    "hero": "Rovato, Erbusco, Iseo, Corte Franca: zona prioritaria. Panne su strade provinciali o fuori cantina — rispondiamo noi.",
    "servizi_intro": "Interventi tra colline, paesi e sponda Iseo.",
    "servizi": [
      ("Pronto Intervento", "Guasto improvviso in Franciacorta: partenza da Brescia verso di te."),
      ("Carro Attrezzi", "Traino a officina locale o Brescia."),
      ("Batteria", "Auto ferma al ristorante o in agriturismo: avviamento sul posto."),
      ("Apertura Porte", "Chiavi chiuse — intervento rapido."),
      ("Moto", "Scooter e moto in zona laghi/colline."),
      ("Rifornimento", "A secco fuori dai paesi: interventiamo."),
    ],
    "steps_intro": "Indica paese e via (o pin): la Franciacorta ha tanti accessi simili.",
    "step3_title": "Arrivo in Franciacorta",
    "step3_p": "Tempi da stima telefonica: dipendono da Rovato vs Iseo vs collina.",
    "perche": [
      "Franciacorta = zona prioritaria",
      "H24 anche weekend «cantine»",
      "Pin WhatsApp preciso",
      "Traino o ripartenza",
      "Preventivo chiaro",
      "No autostrada",
    ],
    "zone_h": "Paesi Franciacorta",
    "zone_p": "Copertura tipica tra Rovato, Erbusco, Iseo e comuni limitrofi.",
    "zones": [
      ("Rovato · Coccaglio", "Nodo viario e residenziale.", ["Rovato", "Coccaglio"], True),
      ("Erbusco · Adro", "Collina e zone produttive.", ["Erbusco", "Adro"], False),
      ("Iseo · Paratico", "Sponda lago e collegamenti.", ["Iseo", "Paratico"], False),
    ],
    "faq": [
      ("Coprite Erbusco di notte?", "Sì, H24."),
      ("Venite anche a Corte Franca?", "Sì, area Franciacorta."),
      ("Traino verso Brescia?", "Sì."),
      ("Numero?", "339 599 8469."),
      ("Solo auto o anche furgoni?", "Anche commerciali leggeri."),
      ("Autostrada?", "No."),
    ],
    "cta": ("In panne in Franciacorta?", "Un messaggio e ci muoviamo."),
    "nap": "Soccorso Stradale Franciacorta",
  },
  {
    "slug": "carro-attrezzi-franciacorta",
    "title": "Carro Attrezzi Franciacorta | Traino Rovato e Iseo",
    "desc": "Carro attrezzi Franciacorta H24: traino a Rovato, Erbusco, Iseo. Solomon 339 599 8469.",
    "kws": "carro attrezzi Franciacorta, traino auto Rovato, carroattrezzi Iseo",
    "place": "Franciacorta",
    "badge": "Carro attrezzi · Franciacorta",
    "h1a": "Carro attrezzi",
    "h1b": "Franciacorta",
    "hero": "Traino professionale tra i paesi della Franciacorta. Destinazione a tua scelta, carico su pianale.",
    "servizi_intro": "Trasporti tipici in zona collinare e verso Brescia.",
    "servizi": [
      ("Traino paesi", "Rovato, Erbusco, Adro, Corte Franca…"),
      ("Verso Iseo", "Consegna sponda lago su accordo."),
      ("Pianale", "Carico sicuro per automatiche e sportive."),
      ("Programmato", "Anche trasferimenti non urgenti."),
      ("Moto", "Attrezzatura dedicata."),
      ("H24", "Emergenze anche di notte."),
    ],
    "steps_intro": "Dimmi punto di ritiro e destinazione.",
    "step3_title": "Consegna dove indichi",
    "step3_p": "Officina locale, Brescia o altro indirizzo concordato.",
    "perche": [
      "Focus Franciacorta",
      "Pianale Iveco",
      "Tempi stimati onesti",
      "H24",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Aree di traino",
    "zone_p": "Franciacorta e rientro verso Brescia.",
    "zones": [
      ("Rovato", "Nodo principale.", ["Rovato"], True),
      ("Collina", "Erbusco, Adro, Provaglio.", ["Erbusco", "Adro"], False),
      ("Iseo", "Sponda e collegamenti.", ["Iseo"], False),
    ],
    "faq": [
      ("Weekend in Franciacorta?", "Sì, operativi."),
      ("Fuori provincia?", "Su accordo."),
      ("Numero?", "339 599 8469."),
      ("Documenti?", "Utili; in emergenza regoliamo dopo."),
      ("Moto?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Serve il carro in Franciacorta?", "Chiamaci."),
    "nap": "Carro Attrezzi Franciacorta",
  },
  {
    "slug": "soccorso-stradale-desenzano",
    "title": "Soccorso Stradale Desenzano del Garda | Carro Attrezzi H24",
    "desc": "Soccorso stradale a Desenzano del Garda H24. Panne, batteria, traino. Solomon 339 599 8469.",
    "kws": "soccorso stradale Desenzano, carro attrezzi Desenzano, pronto intervento Desenzano Garda",
    "place": "Desenzano del Garda",
    "badge": "Desenzano · Lago di Garda 24/7",
    "h1a": "Soccorso a",
    "h1b": "Desenzano",
    "hero": "Auto ferma a Desenzano o lungo la sponda bresciana? Interveniamo H24 — strade urbane e provinciali, non autostrada.",
    "servizi_intro": "Uscite tipiche a Desenzano e dintorni.",
    "servizi": [
      ("Pronto Intervento", "Panne in città, parcheggi, zone residenziali."),
      ("Carro Attrezzi", "Traino a officina Desenzano o verso Brescia."),
      ("Batteria", "Avviamento dopo sosta lunga o freddo."),
      ("Apertura Porte", "Chiavi in auto al lago: interveniamo."),
      ("Moto", "Scooter e moto in zona turistica."),
      ("Rifornimento", "A secco vicino al lago: portiamo carburante."),
    ],
    "steps_intro": "Desenzano: indica quartiere o pin per arrivare al primo colpo.",
    "step3_title": "Verso Desenzano",
    "step3_p": "Partiamo da Brescia: al telefono la stima in base a traffico e punto esatto.",
    "perche": [
      "Sponda bresciana del Garda",
      "H24 anche in stagione",
      "Traino o ripartenza",
      "Pin WhatsApp",
      "Preventivo chiaro",
      "No autostrada",
    ],
    "zone_h": "Desenzano e Garda BS",
    "zone_p": "Desenzano, Sirmione, Salò — sponda bresciana.",
    "zones": [
      ("Desenzano", "Centro, Rivoltella, zone residenziali.", ["Desenzano", "Rivoltella"], True),
      ("Sirmione", "Interventi su richiesta verso la penisola.", ["Sirmione"], False),
      ("Salò · Gardone Riviera", "Sponda nord-ovest BS.", ["Salò", "Gardone Riviera"], False),
    ],
    "faq": [
      ("Tempi per Desenzano?", "Dipendono da ora e traffico: stima al telefono."),
      ("Venite in alta stagione?", "Sì, H24."),
      ("Traino a Sirmione?", "Sì, area Garda BS."),
      ("Numero?", "339 599 8469."),
      ("Solo emergente?", "Anche trasporti concordati."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Desenzano?", "Chiamaci adesso."),
    "nap": "Soccorso Stradale Desenzano",
  },
  {
    "slug": "soccorso-stradale-lago-di-garda",
    "title": "Soccorso Stradale Lago di Garda | Sponda Bresciana H24",
    "desc": "Soccorso stradale Lago di Garda (sponda Brescia): Desenzano, Sirmione, Salò. H24 · 339 599 8469.",
    "kws": "soccorso stradale Lago di Garda, carro attrezzi Garda Brescia, soccorso Desenzano Sirmione",
    "place": "Lago di Garda",
    "badge": "Lago di Garda · sponda BS 24/7",
    "h1a": "Soccorso",
    "h1b": "Lago di Garda",
    "hero": "Sponda bresciana: Desenzano, Sirmione, Salò, Gardone Riviera. Operativi H24 su strade urbane e provinciali.",
    "servizi_intro": "Interventi tipici sulla riviera bresciana.",
    "servizi": [
      ("Pronto Intervento", "Panne in paese o fuori stagione: rispondiamo."),
      ("Carro Attrezzi", "Traino lungo la sponda o verso Brescia."),
      ("Batteria", "Auto ferma dopo sosta lunga al lago."),
      ("Apertura Porte", "Chiavi chiuse in zona turistica."),
      ("Moto", "Due ruote in riviera."),
      ("Rifornimento", "Carburante sul posto se sei a secco."),
    ],
    "steps_intro": "Specifica il paese: Desenzano ≠ Salò ≠ Sirmione.",
    "step3_title": "Arrivo sulla sponda",
    "step3_p": "Stima telefonica in base al comune e al traffico gardesano.",
    "perche": [
      "Focus sponda bresciana",
      "H24",
      "Pin GPS WhatsApp",
      "Traino flessibile",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Paesi Garda BS",
    "zone_p": "Da Desenzano verso nord sulla sponda bresciana.",
    "zones": [
      ("Desenzano · Sirmione", "Sud lago BS.", ["Desenzano", "Sirmione"], True),
      ("Salò · Gardone", "Riviera.", ["Salò", "Gardone Riviera"], False),
      ("Verso Brescia", "Rientro in officina cittadina.", ["Brescia"], False),
    ],
    "faq": [
      ("Coprite anche il Veronese?", "Lavoriamo sulla sponda bresciana; altri casi su valutazione."),
      ("SS45bis?", "Strade provinciali sì; autostrada no."),
      ("Numero?", "339 599 8469."),
      ("Notte in agosto?", "Sì, H24."),
      ("Moto?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("In panne al Garda (BS)?", "Chiamaci."),
    "nap": "Soccorso Stradale Lago di Garda",
  },
  {
    "slug": "soccorso-stradale-gardone-valtrompia",
    "title": "Soccorso Stradale Gardone Val Trompia | H24 Solomon",
    "desc": "Soccorso stradale a Gardone Val Trompia H24. Panne e carro attrezzi. 339 599 8469.",
    "kws": "soccorso stradale Gardone Val Trompia, carro attrezzi Gardone Valtrompia",
    "place": "Gardone Val Trompia",
    "badge": "Gardone Val Trompia · 24/7",
    "h1a": "Soccorso a",
    "h1b": "Gardone V.T.",
    "hero": "Panne a Gardone Val Trompia? Siamo zona prioritaria valle: stima tempi e partenza dal numero diretto.",
    "servizi_intro": "Interventi a Gardone e comuni vicini.",
    "servizi": [
      ("Pronto Intervento", "Guasto in via, cortile o zona artigianale."),
      ("Carro Attrezzi", "Traino locale o verso Brescia."),
      ("Batteria", "Avviamento sul posto."),
      ("Apertura Porte", "Chiavi in auto."),
      ("Moto", "Due ruote in valle."),
      ("Rifornimento", "Carburante di emergenza."),
    ],
    "steps_intro": "Via e civico o pin: a Gardone contano gli accessi.",
    "step3_title": "Verso Gardone",
    "step3_p": "Partenza da Brescia verso la valle — stima al telefono.",
    "perche": [
      "Val Trompia prioritaria",
      "H24",
      "Pin WhatsApp",
      "Traino o ripartenza",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Gardone e vicini",
    "zone_p": "Gardone, Villa Carcina, collegamento valle.",
    "zones": [
      ("Gardone V.T.", "Centro e zone artigianali.", ["Gardone"], True),
      ("Villa Carcina", "Comune limitrofo.", ["Villa Carcina"], False),
      ("Verso Lumezzane", "Continuità valle.", ["Sarezzo", "Lumezzane"], False),
    ],
    "faq": [
      ("Siete di Gardone?", "Sede a Brescia; Val Trompia è prioritaria."),
      ("WhatsApp?", "Sì, 339 599 8469."),
      ("Di domenica?", "Sì."),
      ("Traino officina valle?", "Sì."),
      ("Numero?", "339 599 8469."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Gardone V.T.?", "Chiamaci."),
    "nap": "Soccorso Gardone Val Trompia",
  },
  {
    "slug": "soccorso-stradale-lumezzane",
    "title": "Soccorso Stradale Lumezzane | Pronto Intervento H24",
    "desc": "Soccorso stradale a Lumezzane H24: panne, traino, batteria. Solomon 339 599 8469.",
    "kws": "soccorso stradale Lumezzane, carro attrezzi Lumezzane, auto in panne Lumezzane",
    "place": "Lumezzane",
    "badge": "Lumezzane · Val Trompia 24/7",
    "h1a": "Soccorso a",
    "h1b": "Lumezzane",
    "hero": "Lumezzane: dislivelli e traffico dei turni. Mandaci il punto esatto e organizziamo l'uscita senza call center.",
    "servizi_intro": "Uscite tipiche a Lumezzane.",
    "servizi": [
      ("Pronto Intervento", "Panne in zona residenziale o produttiva."),
      ("Carro Attrezzi", "Traino in valle o Brescia."),
      ("Batteria", "Avviamento sul posto."),
      ("Apertura Porte", "Chiavi chiuse."),
      ("Furgoni", "Commerciali leggeri nei limiti del mezzo."),
      ("Rifornimento", "Carburante di emergenza."),
    ],
    "steps_intro": "Se il civico è difficile, diamoci un riferimento (rotonda, capannone).",
    "step3_title": "Arrivo a Lumezzane",
    "step3_p": "Stima telefonica reale in base a ora e zona.",
    "perche": [
      "Val Trompia prioritaria",
      "Esperienza zona produttiva",
      "H24",
      "Pin GPS",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Lumezzane e valle",
    "zone_p": "Lumezzane e collegamenti verso Gardone/Sarezzo.",
    "zones": [
      ("Lumezzane", "Centro e zone artigianali.", ["Lumezzane"], True),
      ("Gardone V.T.", "Continuità valle.", ["Gardone"], False),
      ("Sarezzo", "Media valle.", ["Sarezzo"], False),
    ],
    "faq": [
      ("Trainate furgoni?", "Leggeri sì, nei limiti."),
      ("Di domenica?", "Sì H24."),
      ("Numero?", "339 599 8469."),
      ("Notte?", "Sì."),
      ("Verso Brescia?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Lumezzane?", "Chiamaci."),
    "nap": "Soccorso Stradale Lumezzane",
  },
  {
    "slug": "soccorso-stradale-sarezzo",
    "title": "Soccorso Stradale Sarezzo | Carro Attrezzi Val Trompia",
    "desc": "Soccorso stradale a Sarezzo H24: panne, batteria, apertura porte e carro attrezzi in Val Trompia. Chiama 339 599 8469.",
    "kws": "soccorso stradale Sarezzo, carro attrezzi Sarezzo, pronto intervento Sarezzo",
    "place": "Sarezzo",
    "badge": "Sarezzo · Val Trompia 24/7",
    "h1a": "Soccorso a",
    "h1b": "Sarezzo",
    "hero": "A Sarezzo per emergenze stradali e traino. Stessa qualità Brescia, tempi pensati per la media valle.",
    "servizi_intro": "Interventi a Sarezzo e dintorni.",
    "servizi": [
      ("Pronto Intervento", "Guasto improvviso: chiama e invita la posizione."),
      ("Carro Attrezzi", "Verso officina Sarezzo/Gardone o Brescia."),
      ("Batteria", "Ripartenza sul posto se possibile."),
      ("Apertura Porte", "Chiavi in auto."),
      ("Moto", "Due ruote."),
      ("Rifornimento", "A secco."),
    ],
    "steps_intro": "In valle chiediamo subito il punto esatto.",
    "step3_title": "Verso Sarezzo",
    "step3_p": "Stima al telefono — niente tempi «da brochure».",
    "perche": [
      "Media Val Trompia",
      "H24",
      "GPS WhatsApp",
      "Traino flessibile",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Sarezzo e vicini",
    "zone_p": "Sarezzo, Villa Carcina, collegamento valle.",
    "zones": [
      ("Sarezzo", "Paese e zone artigianali.", ["Sarezzo"], True),
      ("Villa Carcina", "Limitrofo.", ["Villa Carcina"], False),
      ("Gardone · Lumezzane", "Continuità.", ["Gardone", "Lumezzane"], False),
    ],
    "faq": [
      ("Coprite Villa Carcina?", "Sì."),
      ("Di notte?", "Sì."),
      ("Numero?", "339 599 8469."),
      ("Traino Brescia?", "Sì."),
      ("WhatsApp?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Sarezzo?", "Chiamaci."),
    "nap": "Soccorso Stradale Sarezzo",
  },
  {
    "slug": "soccorso-stradale-rovato",
    "title": "Soccorso Stradale Rovato | Franciacorta H24",
    "desc": "Soccorso stradale a Rovato H24. Panne e carro attrezzi in Franciacorta. 339 599 8469.",
    "kws": "soccorso stradale Rovato, carro attrezzi Rovato, pronto intervento Rovato",
    "place": "Rovato",
    "badge": "Rovato · Franciacorta 24/7",
    "h1a": "Soccorso a",
    "h1b": "Rovato",
    "hero": "Rovato è nodo della Franciacorta: panne in paese o periferia, rispondiamo H24 dal numero diretto.",
    "servizi_intro": "Interventi a Rovato e comuni vicini.",
    "servizi": [
      ("Pronto Intervento", "Guasto in paese o zona produttiva."),
      ("Carro Attrezzi", "Traino locale o Brescia."),
      ("Batteria", "Avviamento sul posto."),
      ("Apertura Porte", "Chiavi chiuse."),
      ("Moto", "Due ruote."),
      ("Rifornimento", "Carburante emergenza."),
    ],
    "steps_intro": "Via o pin: Rovato ha zone simili — meglio essere precisi.",
    "step3_title": "Verso Rovato",
    "step3_p": "Stima telefonica da Brescia verso Franciacorta.",
    "perche": [
      "Franciacorta prioritaria",
      "H24",
      "Pin WhatsApp",
      "Traino o ripartenza",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Rovato e Franciacorta",
    "zone_p": "Rovato, Coccaglio, Erbusco.",
    "zones": [
      ("Rovato", "Centro e periferia.", ["Rovato"], True),
      ("Coccaglio", "Limitrofo.", ["Coccaglio"], False),
      ("Erbusco", "Collina Franciacorta.", ["Erbusco"], False),
    ],
    "faq": [
      ("Tempi da Brescia?", "Stima al telefono."),
      ("Notte?", "Sì."),
      ("Numero?", "339 599 8469."),
      ("Traino Iseo?", "Su percorso Franciacorta sì."),
      ("WhatsApp?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Rovato?", "Chiamaci."),
    "nap": "Soccorso Stradale Rovato",
  },
  {
    "slug": "soccorso-stradale-sirmione",
    "title": "Soccorso Stradale Sirmione | Lago di Garda H24",
    "desc": "Soccorso stradale a Sirmione H24. Panne e traino sponda bresciana. 339 599 8469.",
    "kws": "soccorso stradale Sirmione, carro attrezzi Sirmione, pronto intervento Sirmione",
    "place": "Sirmione",
    "badge": "Sirmione · Garda BS 24/7",
    "h1a": "Soccorso a",
    "h1b": "Sirmione",
    "hero": "A Sirmione accessi e traffico contano: diciamo subito se interveniamo sul punto o concordiamo un carico più comodo.",
    "servizi_intro": "Interventi a Sirmione e collegamento Desenzano.",
    "servizi": [
      ("Pronto Intervento", "Panne in paese o verso la penisola."),
      ("Carro Attrezzi", "Traino verso officina o Desenzano/Brescia."),
      ("Batteria", "Avviamento sul posto."),
      ("Apertura Porte", "Chiavi in auto."),
      ("Moto", "Due ruote in zona turistica."),
      ("Rifornimento", "A secco."),
    ],
    "steps_intro": "Spiega dove sei: centro, Colombare, collegamenti.",
    "step3_title": "Verso Sirmione",
    "step3_p": "Valutiamo accesso e tempi al telefono — onestà prima di partire.",
    "perche": [
      "Sponda bresciana",
      "Valutazione accessi",
      "H24",
      "Pin WhatsApp",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Sirmione e sud Garda BS",
    "zone_p": "Sirmione e Desenzano.",
    "zones": [
      ("Sirmione", "Paese e accessi.", ["Sirmione"], True),
      ("Desenzano", "Collegamento sud lago.", ["Desenzano"], False),
      ("Verso Brescia", "Traino in città.", ["Brescia"], False),
    ],
    "faq": [
      ("Entrate ovunque a Sirmione?", "Dipende da accessi e orari: lo diciamo prima."),
      ("Numero?", "339 599 8469."),
      ("Notte in estate?", "Sì H24."),
      ("Traino Desenzano?", "Sì."),
      ("WhatsApp?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Sirmione?", "Chiamaci."),
    "nap": "Soccorso Stradale Sirmione",
  },
  {
    "slug": "soccorso-stradale-salo",
    "title": "Soccorso Stradale Salò | Lago di Garda H24",
    "desc": "Soccorso stradale a Salò H24. Panne e carro attrezzi sponda bresciana. 339 599 8469.",
    "kws": "soccorso stradale Salò, carro attrezzi Salò, pronto intervento Salò Garda",
    "place": "Salò",
    "badge": "Salò · Garda BS 24/7",
    "h1a": "Soccorso a",
    "h1b": "Salò",
    "hero": "Salò e riviera: interveniamo su strade urbane e provinciali H24. Pin WhatsApp per arrivare giusti.",
    "servizi_intro": "Interventi a Salò e Gardone Riviera.",
    "servizi": [
      ("Pronto Intervento", "Panne in paese o lungo la riviera."),
      ("Carro Attrezzi", "Traino locale o verso Brescia."),
      ("Batteria", "Avviamento sul posto."),
      ("Apertura Porte", "Chiavi chiuse."),
      ("Moto", "Due ruote."),
      ("Rifornimento", "Carburante emergenza."),
    ],
    "steps_intro": "Indica Salò o frazione e un riferimento chiaro.",
    "step3_title": "Verso Salò",
    "step3_p": "Stima da Brescia in base a traffico gardesano.",
    "perche": [
      "Riviera bresciana",
      "H24",
      "Pin GPS",
      "Traino flessibile",
      "Prezzo chiaro",
      "No autostrada",
    ],
    "zone_h": "Salò e riviera",
    "zone_p": "Salò, Gardone Riviera, collegamenti.",
    "zones": [
      ("Salò", "Centro e dintorni.", ["Salò"], True),
      ("Gardone Riviera", "Vicino riviera.", ["Gardone Riviera"], False),
      ("Desenzano", "Sud lago BS.", ["Desenzano"], False),
    ],
    "faq": [
      ("Coprite Gardone Riviera?", "Sì, sponda BS."),
      ("Numero?", "339 599 8469."),
      ("Notte?", "Sì."),
      ("Traino Brescia?", "Sì."),
      ("WhatsApp?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Fermo a Salò?", "Chiamaci."),
    "nap": "Soccorso Stradale Salò",
  },
  {
    "slug": "batteria-auto-scarica-brescia",
    "title": "Batteria Auto Scarica Brescia | Avviamento H24 · Solomon",
    "desc": "Batteria scarica a Brescia? Avviamento o valutazione sul posto H24. 339 599 8469.",
    "kws": "batteria scarica Brescia, avviamento auto Brescia, sostituzione batteria sul posto",
    "place": "Brescia",
    "badge": "Batteria scarica · Brescia 24/7",
    "h1a": "Batteria scarica",
    "h1b": "a Brescia",
    "hero": "Click-click in avviamento o spie spente? Spesso non serve il carro: veniamo per avviamento o valutazione sul posto.",
    "servizi_intro": "Quando la batteria è il problema — Brescia e provincia.",
    "servizi": [
      ("Avviamento", "Tentativo sul posto per evitarti un traino inutile."),
      ("Valutazione", "Se la batteria è morta, ti diciamo le opzioni."),
      ("Notte", "Anche sotto casa alle 3."),
      ("Val Trompia", "Stesso servizio in valle."),
      ("Franciacorta", "Uscite anche in zona collinare."),
      ("Traino breve", "Se non riparte, organizziamo il carro."),
    ],
    "steps_intro": "Descrivi i sintomi: partiamo preparati.",
    "step3_title": "Sul posto",
    "step3_p": "Se riparte, hai risolto. Se no, passiamo al piano B senza giri inutili.",
    "perche": [
      "Spesso senza traino",
      "H24",
      "Brescia + provincia",
      "Onesti sul da farsi",
      "Stesso numero WhatsApp",
      "No autostrada",
    ],
    "zone_h": "Dove interveniamo",
    "zone_p": "Brescia, Val Trompia, Franciacorta, Garda BS.",
    "zones": [
      ("Brescia", "Cortili, parcheggi, strade.", ["Brescia"], True),
      ("Val Trompia", "Gardone, Lumezzane, Sarezzo.", ["Val Trompia"], False),
      ("Franciacorta", "Rovato e paesi.", ["Franciacorta"], False),
    ],
    "faq": [
      ("Quanto dura un avviamento?", "Di solito pochi minuti se l'impianto risponde."),
      ("Vendete batterie?", "Valutazione sul posto; opzioni chiare."),
      ("Auto moderne keyless?", "Dipende: al telefono capiamo."),
      ("Numero?", "339 599 8469."),
      ("Provincia?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Batteria morta?", "Chiamaci — spesso risolviamo sul posto."),
    "nap": "Batteria Scarica Brescia",
  },
  {
    "slug": "apertura-porte-auto-brescia",
    "title": "Apertura Porte Auto Brescia | Chiavi Chiuse in Macchina",
    "desc": "Chiavi chiuse in auto a Brescia? Apertura porte professionale H24. 339 599 8469.",
    "kws": "apertura porte auto Brescia, chiavi chiuse in auto Brescia, apertura auto Brescia",
    "place": "Brescia",
    "badge": "Apertura porte · Brescia 24/7",
    "h1a": "Apertura porte",
    "h1b": "auto Brescia",
    "hero": "Chiavi in macchina e sportelli bloccati: apertura professionale, attenzione a cornici e serrature. Meglio non forzare.",
    "servizi_intro": "Apertura e urgenze correlate a Brescia e provincia.",
    "servizi": [
      ("Apertura", "Tecniche non distruttive quando possibile."),
      ("Modelli critici", "Se è complesso, te lo diciamo prima."),
      ("Notte", "H24 sotto casa o al lavoro."),
      ("Val Trompia", "Stesso servizio in valle."),
      ("Franciacorta", "Uscite in zona collinare."),
      ("Dopo l'apertura", "Se serve traino o batteria, restiamo sul pezzo."),
    ],
    "steps_intro": "Modello auto + dove sei: partiamo informati.",
    "step3_title": "Apriamo e via",
    "step3_p": "Obiettivo: entrare senza danni. Se non è fattibile, lo diciamo prima.",
    "perche": [
      "Approccio non distruttivo",
      "H24",
      "Brescia e provincia",
      "Trasparenza sul modello",
      "Stesso numero",
      "No autostrada",
    ],
    "zone_h": "Zone copertura",
    "zone_p": "Brescia, valli, Franciacorta, Garda BS.",
    "zones": [
      ("Brescia", "Città e quartieri.", ["Brescia"], True),
      ("Provincia", "Val Trompia e Franciacorta.", ["Val Trompia", "Franciacorta"], False),
      ("Garda BS", "Desenzano e sponda.", ["Desenzano"], False),
    ],
    "faq": [
      ("Aprite keyless nuove?", "Dipende dal modello: lo valutiamo al telefono."),
      ("Serve denuncia?", "Di solito no per dimenticanza."),
      ("Numero?", "339 599 8469."),
      ("Notte?", "Sì."),
      ("Provincia?", "Sì."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Chiavi in auto?", "Chiamaci subito."),
    "nap": "Apertura Porte Auto Brescia",
  },
  {
    "slug": "recupero-auto-epoca-brescia",
    "title": "Recupero Auto d'Epoca Brescia | Trasporto Classiche",
    "desc": "Recupero e trasporto auto d'epoca e sportive a Brescia. Pianale protetto. 339 599 8469.",
    "kws": "recupero auto epoca Brescia, trasporto auto classiche Brescia, carro attrezzi Porsche Ferrari",
    "place": "Brescia",
    "badge": "Auto d'epoca · Brescia",
    "h1a": "Auto d'epoca",
    "h1b": "e sportive",
    "hero": "Classiche e sportive non si tirano come un'utilitaria. Pianale con protezioni — collezioni, sportive, trasferimenti.",
    "servizi_intro": "Trasporti dedicati a veicoli di valore.",
    "servizi": [
      ("Pianale protetto", "Cinghie e appoggi, attenzione a spoiler e sottoscocca."),
      ("Emergenza", "Guasto improvviso su auto di valore."),
      ("Programmato", "Da domicilio a officina specializzata."),
      ("Fuori provincia", "Su accordo."),
      ("Eventi", "Logistica per raduni / spostamenti."),
      ("Discrezione", "Trattamento professionale."),
    ],
    "steps_intro": "Descrivi il veicolo e la destinazione.",
    "step3_title": "Carico curato",
    "step3_p": "Meglio 5 minuti in più che un graffio. Carichiamo con calma.",
    "perche": [
      "Esperienza auto di valore",
      "Pianale dedicato",
      "Brescia e oltre su accordo",
      "Preventivo dedicato",
      "Foto interventi reali in galleria",
      "No autostrada",
    ],
    "zone_h": "Partenze tipiche",
    "zone_p": "Brescia, Classic Cars, provincia.",
    "zones": [
      ("Brescia", "Sede e officine specializzate.", ["Brescia"], True),
      ("Provincia", "Ritiri in valle e Franciacorta.", ["Val Trompia", "Franciacorta"], False),
      ("Garda BS", "Ritiri sponda bresciana.", ["Desenzano"], False),
    ],
    "faq": [
      ("Ferrari/Porsche?", "Sì, approccio da collezione."),
      ("Solo emergenza?", "Anche programmato."),
      ("Numero?", "339 599 8469."),
      ("Fuori BS?", "Su accordo."),
      ("Assicurazione?", "Dettagli al telefono prima del carico."),
      ("Autostrada?", "No."),
    ],
    "cta": ("Trasporto auto d'epoca?", "Scrivici su WhatsApp per un preventivo."),
    "nap": "Recupero Auto d'Epoca Brescia",
  },
  {
    "slug": "zone-brescia",
    "title": "Zone di Intervento Brescia e Provincia | Solomon Car Assistance",
    "desc": "Dove interveniamo: Brescia, Val Trompia, Franciacorta, Lago di Garda. Soccorso H24. 339 599 8469.",
    "kws": "zone soccorso stradale Brescia, carro attrezzi provincia Brescia, Val Trompia Franciacorta",
    "place": "Brescia e provincia",
    "badge": "Zone · Brescia e provincia",
    "h1a": "Dove",
    "h1b": "interveniamo",
    "hero": "Non copriamo «tutta Italia»: Brescia e provincia, priorità Val Trompia e Franciacorta, più sponda bresciana del Garda.",
    "servizi_intro": "Stessi servizi, zone diverse — scegli la pagina della tua area.",
    "servizi": [
      ("Brescia città", "Centro e periferia in ~30 min medi."),
      ("Val Trompia", "Gardone, Lumezzane, Sarezzo — priorità."),
      ("Franciacorta", "Rovato, Erbusco, Iseo — priorità."),
      ("Lago di Garda BS", "Desenzano, Sirmione, Salò."),
      ("Batteria / Porte", "Servizi sul posto in tutte le zone."),
      ("Carro attrezzi", "Traino tra zone e verso officina."),
    ],
    "steps_intro": "Se sei in panne: chiama. Se navighi: apri la pagina della tua zona.",
    "step3_title": "Arriviamo da te",
    "step3_p": "Tempi diversi per città e valle: te li diciamo al telefono.",
    "perche": [
      "Zone chiare, niente promesse fake",
      "Priorità Val Trompia e Franciacorta",
      "H24",
      "No autostrada",
      "Numero unico 339 599 8469",
      "Sede Via Tamburini 51",
    ],
    "zone_h": "Mappa operativa",
    "zone_p": "Tre macro-aree: città, valli/Franciacorta, Garda BS.",
    "zones": [
      ("Brescia Città", "Pronto intervento urbano.", ["Centro", "Periferia", "Industrie"], True),
      ("Val Trompia & Franciacorta", "Priorità dichiarate.", ["Gardone", "Lumezzane", "Rovato", "Iseo"], False),
      ("Lago di Garda BS", "Desenzano, Sirmione, Salò.", ["Desenzano", "Sirmione", "Salò"], False),
    ],
    "faq": [
      ("Tutta la provincia?", "Sì su strade urbane/provinciali; tempi variabili."),
      ("Basi in valle?", "Partiamo da Brescia; valli sono prioritarie."),
      ("Autostrada?", "No."),
      ("Numero?", "339 599 8469."),
      ("Trasporto non urgente?", "Sì, su prenotazione."),
      ("WhatsApp?", "Sì."),
    ],
    "cta": ("Non sai che pagina aprire?", "Chiama: ti guidiamo noi."),
    "nap": "Zone Intervento Brescia",
  },
]


def wa(place: str, extra: str = "Potete intervenire?") -> str:
    return f"https://wa.me/393395998469?text={quote(f'Ciao Solomon, sono in panne a {place}. {extra}')}"


def enrich_faq(place: str, faq: list[tuple[str, str]], slug: str) -> list[tuple[str, str]]:
    """FAQ orientate a ricerche di urgenza locali (numero, H24, costo, carro)."""
    out = list(faq)
    existing_l = " ".join(q.lower() for q, _ in out)

    must = []
    # Sempre una FAQ “numero + soccorso stradale + luogo” (query tipica di urgenza)
    if "numero del soccorso" not in existing_l and "numero per il soccorso" not in existing_l:
        must.append(
            (
                f"Qual è il numero del soccorso stradale a {place}?",
                f"Il numero diretto di Solomon Car Assistance è {TEL} (anche WhatsApp), attivo 24/7 per interventi a {place}.",
            )
        )
    if "notte" not in existing_l and "24" not in existing_l and "festiv" not in existing_l:
        must.append(
            (
                f"Il soccorso stradale a {place} è attivo di notte?",
                f"Sì: operativi 24 ore su 24, 7 giorni su 7, anche festivi, a {place} e nei comuni collegati.",
            )
        )
    if "cost" not in existing_l and "prezz" not in existing_l:
        must.append(
            (
                f"Quanto costa il soccorso stradale / carro attrezzi a {place}?",
                "Dipende da tipo di intervento e distanza. Al telefono ti diamo un'indicazione chiara prima di partire, quando possibile.",
            )
        )
    if "carro" in slug and "carro" not in existing_l:
        must.append(
            (
                f"Come richiedo un carro attrezzi a {place}?",
                f"Chiama o scrivi al {TEL}: diciamo dove sei, dove portare il veicolo e partiamo con il pianale.",
            )
        )
    if "batteria" in slug and "avviamento" not in existing_l:
        must.append(
            (
                f"Fate avviamento batteria a {place} senza traino?",
                "Sì, quando possibile partiamo per avviamento sul posto: spesso eviti il carro attrezzi.",
            )
        )
    if "apertura" in slug and "chiav" not in existing_l:
        must.append(
            (
                f"Aprite l'auto se ho lasciato le chiavi dentro a {place}?",
                "Sì: apertura professionale, con attenzione a non danneggiare portiere e serrature quando fattibile.",
            )
        )
    # urgenza generica se manca
    if "pronto intervento" not in existing_l and "panne" not in existing_l:
        must.append(
            (
                f"Fate pronto intervento se l'auto è in panne a {place}?",
                f"Sì: pronto intervento H24 a {place}. Chiama {TEL} e, se puoi, invia la posizione WhatsApp.",
            )
        )

    # prepend must (high-intent) then unique body FAQ
    merged = must + out
    seen = set()
    final = []
    for q, a in merged:
        k = q.lower().strip()
        if k in seen:
            continue
        seen.add(k)
        final.append((q, a))
    return final[:8]  # max 8 FAQ (schema + UX)


# Mesh link: slug -> label (pagine correlate)
LINK_MESH = {
    "soccorso-stradale-brescia": [
        ("carro-attrezzi-brescia", "Carro attrezzi Brescia"),
        ("soccorso-stradale-val-trompia", "Soccorso Val Trompia"),
        ("soccorso-stradale-franciacorta", "Soccorso Franciacorta"),
        ("batteria-auto-scarica-brescia", "Batteria scarica"),
        ("zone-brescia", "Tutte le zone"),
    ],
    "carro-attrezzi-brescia": [
        ("soccorso-stradale-brescia", "Soccorso stradale Brescia"),
        ("carro-attrezzi-val-trompia", "Carro Val Trompia"),
        ("carro-attrezzi-franciacorta", "Carro Franciacorta"),
        ("recupero-auto-epoca-brescia", "Auto d'epoca"),
        ("zone-brescia", "Tutte le zone"),
    ],
    "soccorso-stradale-val-trompia": [
        ("carro-attrezzi-val-trompia", "Carro attrezzi Val Trompia"),
        ("soccorso-stradale-gardone-valtrompia", "Gardone V.T."),
        ("soccorso-stradale-lumezzane", "Lumezzane"),
        ("soccorso-stradale-sarezzo", "Sarezzo"),
        ("soccorso-stradale-brescia", "Brescia città"),
    ],
    "carro-attrezzi-val-trompia": [
        ("soccorso-stradale-val-trompia", "Soccorso Val Trompia"),
        ("soccorso-stradale-lumezzane", "Lumezzane"),
        ("soccorso-stradale-gardone-valtrompia", "Gardone V.T."),
        ("carro-attrezzi-brescia", "Carro Brescia"),
    ],
    "soccorso-stradale-franciacorta": [
        ("carro-attrezzi-franciacorta", "Carro Franciacorta"),
        ("soccorso-stradale-rovato", "Rovato"),
        ("soccorso-stradale-brescia", "Brescia"),
        ("zone-brescia", "Tutte le zone"),
    ],
    "carro-attrezzi-franciacorta": [
        ("soccorso-stradale-franciacorta", "Soccorso Franciacorta"),
        ("soccorso-stradale-rovato", "Rovato"),
        ("carro-attrezzi-brescia", "Carro Brescia"),
    ],
    "soccorso-stradale-desenzano": [
        ("soccorso-stradale-lago-di-garda", "Lago di Garda"),
        ("soccorso-stradale-sirmione", "Sirmione"),
        ("soccorso-stradale-salo", "Salò"),
        ("carro-attrezzi-brescia", "Carro attrezzi"),
    ],
    "soccorso-stradale-lago-di-garda": [
        ("soccorso-stradale-desenzano", "Desenzano"),
        ("soccorso-stradale-sirmione", "Sirmione"),
        ("soccorso-stradale-salo", "Salò"),
        ("zone-brescia", "Tutte le zone"),
    ],
    "soccorso-stradale-gardone-valtrompia": [
        ("soccorso-stradale-val-trompia", "Val Trompia"),
        ("soccorso-stradale-lumezzane", "Lumezzane"),
        ("soccorso-stradale-sarezzo", "Sarezzo"),
    ],
    "soccorso-stradale-lumezzane": [
        ("soccorso-stradale-val-trompia", "Val Trompia"),
        ("soccorso-stradale-gardone-valtrompia", "Gardone V.T."),
        ("carro-attrezzi-val-trompia", "Carro Val Trompia"),
    ],
    "soccorso-stradale-sarezzo": [
        ("soccorso-stradale-val-trompia", "Val Trompia"),
        ("soccorso-stradale-lumezzane", "Lumezzane"),
        ("soccorso-stradale-gardone-valtrompia", "Gardone"),
    ],
    "soccorso-stradale-rovato": [
        ("soccorso-stradale-franciacorta", "Franciacorta"),
        ("carro-attrezzi-franciacorta", "Carro Franciacorta"),
        ("soccorso-stradale-brescia", "Brescia"),
    ],
    "soccorso-stradale-sirmione": [
        ("soccorso-stradale-desenzano", "Desenzano"),
        ("soccorso-stradale-lago-di-garda", "Lago di Garda"),
        ("soccorso-stradale-salo", "Salò"),
    ],
    "soccorso-stradale-salo": [
        ("soccorso-stradale-lago-di-garda", "Lago di Garda"),
        ("soccorso-stradale-desenzano", "Desenzano"),
        ("soccorso-stradale-sirmione", "Sirmione"),
    ],
    "batteria-auto-scarica-brescia": [
        ("soccorso-stradale-brescia", "Soccorso Brescia"),
        ("apertura-porte-auto-brescia", "Apertura porte"),
        ("carro-attrezzi-brescia", "Carro attrezzi"),
    ],
    "apertura-porte-auto-brescia": [
        ("soccorso-stradale-brescia", "Soccorso Brescia"),
        ("batteria-auto-scarica-brescia", "Batteria scarica"),
        ("zone-brescia", "Zone"),
    ],
    "recupero-auto-epoca-brescia": [
        ("carro-attrezzi-brescia", "Carro attrezzi"),
        ("soccorso-stradale-brescia", "Soccorso Brescia"),
        ("zone-brescia", "Zone"),
    ],
    "zone-brescia": [
        ("soccorso-stradale-brescia", "Soccorso Brescia"),
        ("soccorso-stradale-val-trompia", "Val Trompia"),
        ("soccorso-stradale-franciacorta", "Franciacorta"),
        ("soccorso-stradale-lago-di-garda", "Lago di Garda"),
        ("carro-attrezzi-brescia", "Carro attrezzi"),
    ],
}


def render_related(slug: str) -> str:
    links = LINK_MESH.get(slug, [("zone-brescia", "Tutte le zone"), ("", "Home")])
    lis = []
    for s, lab in links:
        href = f"/{s}.html" if s else "/"
        lis.append(f'<li><a href="{href}" style="color:#ffb400">{lab}</a></li>')
    return (
        '<div class="seo-related" style="margin-top:20px;text-align:center">'
        '<p style="color:rgba(255,255,255,.7);margin-bottom:8px;font-size:.88rem">Pagine collegate</p>'
        f'<ul style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px 16px;list-style:none;padding:0;margin:0">{"".join(lis)}</ul>'
        "</div>"
    )


def page_service_schema(p: dict, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"{p['h1a']} {p['h1b']}".strip(),
        "serviceType": "Soccorso Stradale / Carro Attrezzi",
        "description": p["desc"],
        "url": url,
        "provider": {"@id": f"{BASE}/#organization"},
        "areaServed": {"@type": "Place", "name": p["place"]},
        "availableChannel": {
            "@type": "ServiceChannel",
            "servicePhone": {
                "@type": "ContactPoint",
                "telephone": TEL_E,
                "contactType": "customer service",
                "areaServed": p["place"],
                "availableLanguage": ["Italian"],
                "hoursAvailable": "Mo-Su 00:00-23:59",
            },
        },
        "offers": {
            "@type": "Offer",
            "availability": "https://schema.org/InStock",
            "priceCurrency": "EUR",
        },
    }


def page_emergency_schema(p: dict) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "@id": f"{BASE}/{p['slug']}.html#emergency",
        "name": f"Solomon Car Assistance – {p['nap']}",
        "telephone": TEL_E,
        "openingHours": "Mo-Su 00:00-23:59",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Via Pietro Tamburini 51",
            "addressLocality": "Brescia",
            "addressRegion": "Lombardia",
            "postalCode": "25136",
            "addressCountry": "IT",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 45.5784035, "longitude": 10.2310602},
        "areaServed": p["place"],
        "availableLanguage": "Italian",
        "url": f"{BASE}/{p['slug']}.html",
    }


def render_servizi(cards: list[tuple[str, str]]) -> str:
    icons = [
        "fa-car-crash",
        "fa-truck-moving",
        "fa-motorcycle",
        "fa-bolt",
        "fa-key",
        "fa-gas-pump",
    ]
    parts = []
    for i, ((title, p), icon) in enumerate(zip(cards, icons)):
        parts.append(
            f"""      <div class="servizio-card" data-animate>
        <div class="card-icon"><i class="fas {icon}"></i></div>
        <h3>{title}</h3>
        <p>{p}</p>
      </div>"""
        )
    return "\n".join(parts)


def render_zones(zones: list) -> str:
    out = []
    for title, p, luoghi, featured in zones:
        feat = " zona-card--featured" if featured else ""
        badge = '\n        <span class="zona-badge">Area principale</span>' if featured else ""
        icon = "fa-city" if featured else ("fa-map" if "Trompia" in title or "Franciacorta" in title or "Provincia" in title or "valle" in title.lower() else "fa-water")
        if "Garda" in title or "Desenzano" in title or "Sirmione" in title or "Salò" in title or "Salò" in title:
            icon = "fa-water"
        if "Val Trompia" in title or "Gardone" in title or "Lumezzane" in title or "Sarezzo" in title or "Franciacorta" in title or "Rovato" in title:
            icon = "fa-map"
        if "Brescia" in title and "Città" in title or title.startswith("Brescia") or title.startswith("Officine"):
            icon = "fa-city"
        lis = "".join(f"<li>{x}</li>" for x in luoghi)
        out.append(
            f"""      <article class="zona-card{feat}" data-animate>
        <div class="zona-icon"><i class="fas {icon}"></i></div>
        <h3>{title}</h3>
        <p>{p}</p>
        <ul class="zona-luoghi">{lis}</ul>{badge}
      </article>"""
        )
    return "\n".join(out)


def render_faq(faq: list[tuple[str, str]]) -> str:
    parts = []
    for q, a in faq:
        parts.append(
            f"""      <details class="faq-item" data-animate>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>"""
        )
    return "\n".join(parts)


def render_perche(items: list[str]) -> str:
    return "\n".join(f'        <li><i class="fas fa-check"></i> {it}</li>' for it in items)


def build_page(index: str, p: dict) -> str:
    html = index
    # togli blocco link home (se presente) — le landings usano mesh propria
    html = re.sub(
        r'\s*<div class="seo-hub-home"[^>]*>.*?</div>\s*',
        "\n",
        html,
        count=1,
        flags=re.S,
    )
    url = f"{BASE}/{p['slug']}.html"
    w = wa(p["place"])
    faq = enrich_faq(p["place"], p["faq"], p["slug"])

    # Head essentials
    html = re.sub(r"<title>.*?</title>", f"<title>{p['title']}</title>", html, count=1, flags=re.S)
    html = re.sub(
        r'<meta name="description" content="[^"]*"/>',
        f'<meta name="description" content="{p["desc"]}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="keywords" content="[^"]*"/>',
        f'<meta name="keywords" content="{p["kws"]}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<link rel="canonical" href="[^"]*"/>',
        f'<link rel="canonical" href="{url}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<link rel="alternate" hreflang="it" href="[^"]*"/>',
        f'<link rel="alternate" hreflang="it" href="{url}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="[^"]*"/>',
        f'<link rel="alternate" hreflang="x-default" href="{url}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="geo.placename" content="[^"]*"/>',
        f'<meta name="geo.placename" content="{p["place"]}, Lombardia, Italia"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]*"/>',
        f'<meta property="og:url" content="{url}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*"/>',
        f'<meta property="og:title" content="{p["title"]}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*"/>',
        f'<meta property="og:description" content="{p["desc"]}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:title" content="[^"]*"/>',
        f'<meta name="twitter:title" content="{p["title"]}"/>',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:description" content="[^"]*"/>',
        f'<meta name="twitter:description" content="{p["desc"]}"/>',
        html,
        count=1,
    )

    # FAQ schema (enriched, urgenza locale)
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)},
            }
            for q, a in faq
        ],
    }
    html = re.sub(
        r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"FAQPage".*?</script>',
        f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>',
        html,
        count=1,
        flags=re.S,
    )

    crumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Zone", "item": f"{BASE}/zone-brescia.html"},
            {"@type": "ListItem", "position": 3, "name": p["place"], "item": url},
        ],
    }
    html = re.sub(
        r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"BreadcrumbList".*?</script>',
        f'<script type="application/ld+json">{json.dumps(crumb_ld, ensure_ascii=False)}</script>',
        html,
        count=1,
        flags=re.S,
    )

    # Service schema → specifico per pagina (non restare su “Brescia” generico)
    svc = page_service_schema(p, url)
    html = re.sub(
        r'<!-- SCHEMA: Service – Pronto Intervento -->\s*<script type="application/ld\+json">.*?</script>',
        "<!-- SCHEMA: Service – pagina locale -->\n  "
        f'<script type="application/ld+json">{json.dumps(svc, ensure_ascii=False)}</script>',
        html,
        count=1,
        flags=re.S,
    )

    # EmergencyService → areaServed della pagina
    em = page_emergency_schema(p)
    html = re.sub(
        r'<!-- SCHEMA: Vehicle/Service equipment -->\s*<script type="application/ld\+json">\s*\{[^}]*"@type":\s*"EmergencyService".*?</script>',
        "<!-- SCHEMA: EmergencyService locale -->\n  "
        f'<script type="application/ld+json">{json.dumps(em, ensure_ascii=False)}</script>',
        html,
        count=1,
        flags=re.S,
    )

    # Logo / nav → home + anchors on this page
    html = html.replace(
        'href="#home" class="header-logo"',
        'href="/" class="header-logo"',
        1,
    )
    html = html.replace(
        """    <nav class="nav" id="nav" role="navigation" aria-label="Menu principale">
      <ul>
        <li><a href="#servizi">Servizi</a></li>
        <li><a href="#specialita">Auto d'Epoca</a></li>
        <li><a href="#galleria">Galleria</a></li>
        <li><a href="#zone">Zone</a></li>
        <li><a href="#recensioni">Recensioni</a></li>
        <li><a href="#posizione">Posizione</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#contatti">Contatti</a></li>
      </ul>
    </nav>""",
        """    <nav class="nav" id="nav" role="navigation" aria-label="Menu principale">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="#servizi">Servizi</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#posizione">Posizione</a></li>
        <li><a href="#contatti">Contatti</a></li>
      </ul>
    </nav>""",
        1,
    )

    # Hero badge + h1 + desc
    html = re.sub(
        r'<span class="hero-badge"><span class="hero-badge-dot"></span>.*?</span>',
        f'<span class="hero-badge"><span class="hero-badge-dot"></span> {p["badge"]}</span>',
        html,
        count=1,
        flags=re.S,
    )
    # second badge desktop
    html = re.sub(
        r'(<span class="hero-badge hero-bottom-badge"[^>]*>)<span class="hero-badge-dot"></span>.*?</span>',
        rf'\1<span class="hero-badge-dot"></span> {p["badge"]}</span>',
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'<h1 style="margin-bottom:8px">\s*<span class="hero-line1">.*?</span>\s*<span class="hero-line2">.*?</span>\s*</h1>',
        f'<h1 style="margin-bottom:8px">\n'
        f'        <span class="hero-line1">{p["h1a"]}</span>\n'
        f'        <span class="hero-line2">{p["h1b"]}</span>\n'
        f"      </h1>",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'<p class="hero-desc">\s*.*?\s*</p>',
        f'<p class="hero-desc">\n        {p["hero"]}\n      </p>',
        html,
        count=1,
        flags=re.S,
    )

    # WA links in hero - replace common Brescia WA texts
    html = re.sub(
        r'https://wa\.me/393395998469\?text=[^"\s]+',
        w,
        html,
    )

    # Servizi section
    html = re.sub(
        r'(<h2 id="h-servizi">I nostri servizi</h2>\s*<p>)(.*?)(</p>)',
        rf"\1{p['servizi_intro']}\3",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'<div class="servizi-grid">.*?</div>\s*</div>\s*</section>\s*\n\n<!-- COME FUNZIONA -->',
        f'<div class="servizi-grid">\n{render_servizi(p["servizi"])}\n    </div>\n  </div>\n</section>\n\n<!-- COME FUNZIONA -->',
        html,
        count=1,
        flags=re.S,
    )

    # Steps
    html = re.sub(
        r'(<h2 id="h-steps">Come funziona</h2>\s*<p>)(.*?)(</p>)',
        rf"\1{p['steps_intro']}\3",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(<div class="step-card step-card--gold"[^>]*>.*?)<h3>.*?</h3>\s*<p>.*?</p>',
        rf'\1<h3>{p["step3_title"]}</h3>\n        <p>{p["step3_p"]}</p>',
        html,
        count=1,
        flags=re.S,
    )

    # Perche list
    html = re.sub(
        r'<ul class="perche-list">.*?</ul>',
        f'<ul class="perche-list">\n{render_perche(p["perche"])}\n      </ul>',
        html,
        count=1,
        flags=re.S,
    )

    # Zone
    html = re.sub(
        r'(<h2 id="h-zone">)Dove interveniamo(</h2>\s*<p>)(.*?)(</p>)',
        rf'\1{p["zone_h"]}\2{p["zone_p"]}\4',
        html,
        count=1,
        flags=re.S,
    )
    # zone-grid: NON usare regex non-greedy (si ferma al primo </div> interno)
    zg = html.find('<div class="zone-grid">')
    nap = html.find('<div class="nap-block">', zg if zg >= 0 else 0)
    if zg >= 0 and nap > zg:
        html = (
            html[:zg]
            + f'<div class="zone-grid">\n{render_zones(p["zones"])}\n    </div>\n    '
            + html[nap:]
        )
    html = re.sub(
        r'(<strong>Solomon Car Assistance</strong> – ).*?(<span class="nap-sep">)',
        rf'\1{p["nap"]} \2',
        html,
        count=1,
        flags=re.S,
    )

    # FAQ
    html = re.sub(
        r'<div class="faq-grid">.*?</div>\s*</div>\s*</section>\s*\n\n<!-- GEOLOCALIZZATORE -->',
        f'<div class="faq-grid">\n{render_faq(faq)}\n    </div>\n  </div>\n</section>\n\n<!-- GEOLOCALIZZATORE -->',
        html,
        count=1,
        flags=re.S,
    )

    # CTA final
    html = re.sub(
        r'(<div class="cta-final-text">\s*<h2>).*?(</h2>\s*<p>).*?(</p>)',
        rf'\1{p["cta"][0]}\2{p["cta"][1]}\3',
        html,
        count=1,
        flags=re.S,
    )

    # Footer home links
    html = html.replace('<li><a href="#home">Home</a></li>', '<li><a href="/">Home</a></li>', 1)

    # Cache bust note on css already exists
    html = html.replace("style.css?v=20261009fixscroll", "style.css?v=20261009fixscroll", 1)

    # Rimuovi intera sezione ZONE (card + nap + link SEO) — non piace sul design
    html = re.sub(
        r'\s*<!-- ZONE -->\s*<section class="section zone"[^>]*>.*?</section>\s*(?=<!-- GALLERIA)',
        "\n\n",
        html,
        count=1,
        flags=re.S,
    )
    # safety: togli eventuali blocchi link SEO residui
    html = re.sub(r'\s*<div class="seo-related"[^>]*>.*?</div>\s*', "\n", html, flags=re.S)
    html = re.sub(r'\s*<div class="seo-hub-home"[^>]*>.*?</div>\s*', "\n", html, flags=re.S)

    return html


def write_sitemap(slugs: list[str]) -> None:
    parts = [
        f"  <url>\n    <loc>{BASE}/</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>"
    ]
    for s in slugs:
        pr = "0.9" if any(x in s for x in ("brescia", "val-trompia", "franciacorta", "desenzano", "zone")) else "0.8"
        parts.append(
            f"  <url>\n    <loc>{BASE}/{s}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(parts)
        + "\n</urlset>\n",
        encoding="utf-8",
    )


def clean_home(index: str) -> str:
    """Togli hub SEO + intera sezione ZONE (card) — non piace su nessuna pagina."""
    index = re.sub(r'\s*<div class="seo-hub-home"[^>]*>.*?</div>\s*', "\n", index, flags=re.S)
    index = re.sub(
        r'\s*<!-- ZONE -->\s*<section class="section zone"[^>]*>.*?</section>\s*(?=<!-- GALLERIA)',
        "\n\n",
        index,
        count=1,
        flags=re.S,
    )
    index = index.replace('<li><a href="#zone">Zone</a></li>\n', "")
    index = index.replace(
        '{"@type":"ListItem","position":3,"name":"Zone","item":"https://solomoncarassistance.it/#zone"},'
        '{"@type":"ListItem","position":4,"name":"Contatti","item":"https://solomoncarassistance.it/#contatti"}',
        '{"@type":"ListItem","position":3,"name":"Contatti","item":"https://solomoncarassistance.it/#contatti"}',
    )
    # Footer slim: P.IVA + REA doar in Privacy modal
    index = index.replace(
        "<p>&copy; 2026 Solomon Car Assistance di Solomon Eugeniu — P.IVA IT04659930988 — REA BS-631269 — Soccorso Stradale Brescia 24/7. Tutti i diritti riservati.</p>",
        "<p>&copy; 2026 Solomon Car Assistance</p>",
    )
    return index


def main() -> None:
    index_path = ROOT / "index.html"
    raw = index_path.read_text(encoding="utf-8")
    index = clean_home(raw)
    if index != raw:
        print("home: removed Pagine zona hub")
    index_path.write_text(index, encoding="utf-8")
    slugs = []
    for p in PAGES:
        out = build_page(index, p)
        (ROOT / f"{p['slug']}.html").write_text(out, encoding="utf-8")
        slugs.append(p["slug"])
        print("ok", p["slug"], "no-zone", "zone" not in out[out.find("<!-- PERCHÉ"):out.find("<!-- GALLERIA")] if "<!-- PERCHÉ" in out else "n/a")
    write_sitemap(slugs)
    print("DONE", len(slugs))


if __name__ == "__main__":
    main()
