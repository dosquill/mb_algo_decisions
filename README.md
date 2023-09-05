# mb_algo_decisions
---

# 1. Problema

Ogni offerta è una riga della tabella fornita sotto. Il budget a disposizione è 3000€. Ogni step si compone di x offerte. Per decidere in ogni step quante offerte fare si deve tener conto che: Per completare un offerta va sottratto al budget iniziale il budget per il completamento dell’offerta situato in “Budget average” dell’offerta. Una volta terminato il budget iniziale a disposizione lo step viene chiuso e si risolvono le offerte. Per lo step successivo: Dopo il conseguimento delle offerte dello step precedente, il budget iniziale va aggiornato con il guadagno derivante dall’offerta e il budget, prima allocato, diventa di nuovo disponibile se l’offerta è stata completata. Si risolve lo step come quello precedente

## 1.1 Domanda

Domanda: Come possiamo fare tutte le offerte disponibili massimizzando il rendimento, il budget e il guadagno? Risolvi questo problema schematizzando una strategia e offrendo una simulazione attuando la strategia, iterando gli step fino al completamento di tutte le offerte disponibili.

# 2. Tabella

I dati che servono per la risoluzione del problema sono in questo file

https://docs.google.com/spreadsheets/d/1zQEq0Z69iEGfztojEk4b6il0ly6FEhAbxj_Zygg97o0/edit

# 3. Schematizzazione delle operazioni

https://xmind.works/share/kllOCyb3


### Useful plugin
mypy


### Useful commands
git log --graph --decorate --oneline
git log --graph
gitk


## Altro
Dati iniziali: 
Ogni offerta è una riga della tabella fornita sotto.
Il budget a disposizione è 3000€.
Ogni step si compone di x offerte.
Per decidere in ogni step quante offerte fare si deve tener conto che:
Per completare un offerta va sottratto al budget iniziale il budget per il completamento dell’offerta situato in “Budget average” dell’offerta.
Una volta terminato il budget iniziale a disposizione lo step viene chiuso e si risolvono le offerte.
Per lo step successivo:
Dopo il conseguimento delle offerte dello step precedente, il budget iniziale va aggiornato con il guadagno derivante dall’offerta e il budget, prima allocato, diventa di nuovo disponibile se l’offerta è stata completata.
Si risolve lo step come quello precedente

Domanda:
Come possiamo fare tutte le offerte disponibili massimizzando il rendimento, il budget e il guadagno?
Risolvi questo problema schematizzando una strategia e offrendo una simulazione attuando la strategia, iterando gli step fino al completamento di tutte le offerte disponibili.


This is the date for solving the problem:
Bookmaker,Earning min,Earning average,Earning max,Budget min,Budget average,Budget max,ROI,Operativo,Quota Minima qualificante,Quota minima bonus,Tipo di Offerta,Condizioni sblocco,Metodi Non Validi,Link offerta,Difficoltà (arbitraria),Tempistiche approssimative conclusione offerta (in gg) Bwin,"€ 8,00","€ 8,50","€ 9,00","€ 40,00","€ 50,00","€ 60,00","17,00%",TRUE,2,2,Scommetti € Ricevi €,,"PayPal, Skrill/Moneybookers, Neteller, Revolut",,4,1 Williamhill,"€ 40,00","€ 45,00","€ 50,00","€ 300,00","€ 325,00","€ 350,00","13,85%",TRUE,2,2,Multipla,,,https://promozioni.williamhill.it/offer/bonus-ita125,6,30 Bet365,"€ 50,00","€ 70,00","€ 90,00","€ 600,00","€ 700,00","€ 800,00","10,00%",TRUE,1.50,1.50,Rollover,6x bonus = max 600€,Entropay/Neteller/Skrill/Moneybookers/Paysafecard,,1,7 Planetwin365,"€ 200,00","€ 220,00","€ 240,00","€ 2.500,00","€ 2.500,00","€ 2.500,00","8,80%",FALSE,2,2,Rollover,8x importo bonus,"Skrill, Neteller",https://www.planetwin365.it/it/promozioni,4,7 Eurobet,"€ 190,00","€ 200,00","€ 210,00","€ 1.750,00","€ 2.375,00","€ 3.000,00","8,42%",FALSE,4,4,Multipla,,"Skrill/Moneybookers, Neteller, Paysafe",https://www.eurobet.it/it/promo/#!/nuovi-iscritti/welcome-bonus-scommesse-1819-21-20210610094120233,7,8 Snai,"€ 200,00","€ 210,00","€ 220,00","€ 3.000,00","€ 3.000,00","€ 3.000,00","7,00%",FALSE,1.25,1.5,Rollover,8x max 2400€,,https://www.snai.it/promozioni/scommesse/bonus-benvenuto-scommesse,8,10 Leovegas,"€ 60,00","€ 90,00","€ 120,00","€ 1.200,00","€ 1.400,00","€ 1.600,00","6,43%",FALSE,1.8,1.8,Scommetti € Ricevi €,,"Skrill, Neteller",https://www.leovegas.it/it-it/promozioni/bonus/s,7,10 Domusbet,"€ 25,00","€ 30,00","€ 35,00","€ 500,00","€ 550,00","€ 600,00","5,45%",FALSE,5,5,Multipla,,,https://www.domusbet.it/bonus-benvenuto_100finoa50,,10 Unibet,"€ 4,00","€ 6,00","€ 8,00","€ 120,00","€ 120,00","€ 120,00","5,00%",FALSE,1.4,,Rollover,8x importo bonus = max 80€,"Skrill, Neteller, Paysafecard",,5,14 E-play24,"€ 14,00","€ 17,00","€ 20,00","€ 400,00","€ 450,00","€ 500,00","3,78%",FALSE,2.5,3,Multipla,,,https://href.li/?https://promozioni.eplay24.it/bonus-benvenuto-sport/,,3 Novibet,"€ 18,00","€ 21,00","€ 24,00","€ 800,00","€ 800,00","€ 800,00","2,63%",FALSE,4,4,Scommetti € Ricevi €,,,https://www.novibet.it/scommesse/promozioni/bonus-benvenuto,,7 Starcasino,"€ 10,00","€ 11,00","€ 12,00","€ 500,00","€ 550,00","€ 600,00","2,00%",FALSE,1.5,8,Multipla,,,,10,10 Bwin 2 (personale),,,,,,,,FALSE,,,,,,,4,

