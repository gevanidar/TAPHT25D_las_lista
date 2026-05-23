# Frågor och svar

## Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

### Svar:

Ett enhetstest 'r gjort f;r att testa en specifik del at programmet. En del kan vara t.ex. en klass eller funktion. Enhetstester f;r funktioner testar att funktionen fungerar korrekt, och f;r klasser s[ kan man skapa enhetstester f;r hela klassen f;r att se till att klassens delar uppn[r det som 'r avsett. Acceptans kriterier anv'nds f;r att s'rskilja vad som 'r korrekt implementation. Enhetstest f;r en klass som kan utf;ra addition, subtraktion, multiplikation och division kommer beh;va verifiera att resultatet fr[n varje funktion blir matematiskt korrekt. Det beh;ver ocks[ verifiera att det inte blir fel vid input, som t.ex. division med 0 ska inte orsaka att programmet kraschar - utan ist'llet ge ett felmeddelande.
Integrationstester 'r tester f;r att se att de olika delarna av programmet fungerar tillsammans. H'r testas sammankopplinger mellan olika funktioner eller klasser och d'r man ser till att de fungerar tillsammans. T.ex. s[ kan en klass f;r en kalkylator och ovan n'mnda klass f;r matematiska ber'kningar beh;vas testas tillsammans, en anv'ndare kan skriva in siffror och tecken i kalkylatorn. Matematik klassen hanterar ber;kningarna, men kopplingen mellan dem m[ste fungera korrekt. Verifiering att input bara inneh[ller siffror och tecken `+`, `-`, `*` samt `/` beh;ver g;ras. Det g[r inte bara att testa att kalkylatorn kan ta input och ge output till anv'ndaren, kopplingen m[ste testas.
Regressionstester 'r till f;r att se hur 'ndringar som g;rs i programmer inte p[verkar den ursprungliga funktionaliteten. Om vi uppt'cker en bugg i kalkylatorn ovan som till[ter att vi skickar in o;nskade tecken och denna bug fixas, s[ kan regressiontestet se till att det gamla acceptans kriteriet f;r kalkylatorns funktion inte g[r s'nder, t.ex. att man fortfarande kan skriva in de matematiska symbolerna..
Prestandatester 'r till f;r att se hur 'ndringar av delar av programmet p[verkar prestandan. Prestanda tester kan anv'ndas f;r att se till att funktioner inte p[verkas negativt av 'ndringar i funktionen, det 'r inte viktigt f;r prestanda tester att funktionen 'r korrekt (det sk;ter de andra testerna). De kan anv'ndas som en benchmark f;r att se till att 'ndringar i koden g;r att koden f;rblir lika bra eller att den f;rb'ttras. Exempel p[ prestandatester 'r ofta baserade p[ hur l[ng tid det tar att utf;ra t.ex. en funktion, m'ngden minne som anv'nds vid en funktion kan ocks[ anv'ndas som ett prestandatest.



## Beskriv hur det går till när man arbetar med TDD.

### Svar:

Test drivern utveckling bygger p[ att man f;rst skriver tester som 'r till f;r att verifiera att den kod man sedan skriver kommer att uppfylla krav eller acceptans kriterier.
En kund s'ger att de vill ha en ny funktion. T.ex. kan denna funktion vara att man ska kunna favoritmarkera b;ckerna i i listan p[ hemsidan och att man sedan ska kunna se vilka b;cker man markerat som favoriter. Detta krav fr[n kunden delas sedan in i User Stories, h'r ska det finnas en user story som hantera att man kan favoritmarkera en bok, en att man kan avmarkera favoriter och en d'r det finns en lista som anv'ndaren kan se ;ver alla markerade favoritb;cker. Det var inte explicit fr[n kunden att man beh;ver kunna avmarkera favoriter, det kan vara bra att diskutera med kunden f;rst om det 'r n[got som de vill ha eller inte (i detta fallet var det en v'ldigt enkel och n;dv'ndig funktion). En user story skrivs p[ s'tter `Som en ..., vill jag ..., s[ att jag ...`. Exempel `Som en anv'ndare, vill jag kunna favoritmarkera en bok, s[ att jag kan h[lla ordning p[ mina favoritb;cker`. Det skrivs ocks[ acceptanskriterier f;r funktionen f;r att man konkret ska kunna verifiera att implementationen av den nya funktionen blir korrekt. En user story tas upp av en testare som skriver ett eller flera tester f;r att s'kerst'lla att funktionen blir r'tt. Det viktiga steget h'r 'r att testerna inte g[r igenom (det blir r;tt) vid f;rsta k;rningen av testerna, eftersom funktionen inte 'r utvecklad s[ ska den inte fungera, om ett test hade g[tt igenom direkt s[ g[r det inte att s'kerst'lla att utvecklingen av den nya funktionen gjort att testet g[tt igenom. En utvecklare skriver sedan kod som g;r att testet g[r igenom, dvs g[r fr[n r;tt till gr;nt. N'r utvecklaren har gjort sin f;rsta implementation s[ g[r hen vidare med att se till att refaktorisera och se till att funktionen upph[ller de standarder eller regler man har p[ f;retaget. N'r funktionen fungerar men 'r l[ngsam prestandatester vara bra att anv'nda (d[ blir det en ny tdd cykel). N'r utvecklaren 'r klar med att fixa allt s[ skickas koden vidare till granskning (det 'r utanf;r TDD cykeln men industristandard).

## Beskriv hur BDD skiljer sig från TDD.

### Svar:

- [ ] TODO: Skriv ett bra svar

## Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

### Svar:

- [ ] TODO: Skriv ett bra svar

