# Frågor och svar

## Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

### Svar:

Ett enhetstest 'r gjort f;r att testa en specifik del at programmet. En del kan vara t.ex. en klass eller funktion. Enhetstester f;r funktioner testar att funktionen fungerar korrekt, och f;r klasser s[ kan man skapa enhetstester f;r hela klassen f;r att se till att klassens delar uppn[r det som 'r avsett. Acceptans kriterier anv'nds f;r att s'rskilja vad som 'r korrekt implementation. Enhetstest f;r en klass som kan utf;ra addition, subtraktion, multiplikation och division kommer beh;va verifiera att resultatet fr[n varje funktion blir matematiskt korrekt. Det beh;ver ocks[ verifiera att det inte blir fel vid input, som t.ex. division med 0 ska inte orsaka att programmet kraschar - utan ist'llet ge ett felmeddelande.
Integrationstester 'r tester f;r att se att de olika delarna av programmet fungerar tillsammans. H'r testas sammankopplinger mellan olika funktioner eller klasser och d'r man ser till att de fungerar tillsammans. T.ex. s[ kan en klass f;r en kalkylator och ovan n'mnda klass f;r matematiska ber'kningar beh;vas testas tillsammans, en anv'ndare kan skriva in siffror och tecken i kalkylatorn. Matematik klassen hanterar ber;kningarna, men kopplingen mellan dem m[ste fungera korrekt. Verifiering att input bara inneh[ller siffror och tecken `+`, `-`, `*` samt `/` beh;ver g;ras. Det g[r inte bara att testa att kalkylatorn kan ta input och ge output till anv'ndaren, kopplingen m[ste testas.
Regressionstester 'r till f;r att se hur 'ndringar som g;rs i programmer inte p[verkar den ursprungliga funktionaliteten. Om vi uppt'cker en bugg i kalkylatorn ovan som till[ter att vi skickar in o;nskade tecken och denna bug fixas, s[ kan regressiontestet se till att det gamla acceptans kriteriet f;r kalkylatorns funktion inte g[r s'nder, t.ex. att man fortfarande kan skriva in de matematiska symbolerna..
Prestandatester 'r till f;r att se hur 'ndringar av delar av programmet p[verkar prestandan. Prestanda tester kan anv'ndas f;r att se till att funktioner inte p[verkas negativt av 'ndringar i funktionen, det 'r inte viktigt f;r prestanda tester att funktionen 'r korrekt (det sk;ter de andra testerna). De kan anv'ndas som en benchmark f;r att se till att 'ndringar i koden g;r att koden f;rblir lika bra eller att den f;rb'ttras. Exempel p[ prestandatester 'r ofta baserade p[ hur l[ng tid det tar att utf;ra t.ex. en funktion, m'ngden minne som anv'nds vid en funktion kan ocks[ anv'ndas som ett prestandatest.



## Beskriv hur det går till när man arbetar med TDD.

### Svar:

- [ ] TODO: Skriv ett bra svar

## Beskriv hur BDD skiljer sig från TDD.

### Svar:

- [ ] TODO: Skriv ett bra svar

## Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

### Svar:

- [ ] TODO: Skriv ett bra svar

