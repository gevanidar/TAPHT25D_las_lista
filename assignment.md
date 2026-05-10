# Examination

Testverktyg, TAP HT25D
Du ska lösa uppgiften självständigt. När du tar hjälp av AI, eller diskuterar med andra studerande, ska du se till att du förstår vad koden gör.

- Bakgrund
- Backend
- Frontend
- Detta ska du göra
- Inlämning
- För G krävs
- För VG krävs
- Tips

--- 

## Bakgrund

"Läslistan" är en webbsida där man kan välja ut sina favoriter från en katalog med böcker, eller lägga till nya. Beställaren är en organisation som vill öka studenters läsande genom att rikta in sig på lättlästa böcker med tekniskt djup. Nuvarande version har begränsad funktionalitet. På sikt vill man utöka webbsidan med funktioner för att dela sina listor, skapa quiz och diskutera böcker med varandra. Därför är det viktigt att det finns tester för all grundläggande funktionalitet. Detta är din uppgift!

För att lösa uppgiften kommer du att arbeta både med frontend och backend. Du ska använda de tekniker som gåtts igenom i kursen.

Webbsidan som ska testas: https://tap-ht25-testverktyg.github.io/exam/ 
(För den som är intresserad av JavaScript och React finns källkoden i ett repo i kursens GitHub-organisation.)

Börja med att läsa igenom hela uppgiften.

--- 

## Backend

Läslistan behöver Python-kod som hanterar listan med böcker. Du kan se exempel på lista här (JavaScript, denna används av webbsidan). Du får lägga till fler klasser och metoder om du behöver.
klassen BookStore ska ha följande metoder:
addBook(author, title)
toggleFavorite(book_id)
klassen FavoriteBooks ska ha följande metoder:
add(book)
remove(book)

### Med hjälp av TDD ska du:

skriva enhetstest för alla metoder
skriva integrationstest för klasserna

### Teorifrågor

Dessutom ska du svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
Beskriv hur det går till när man arbetar med TDD.
Beskriv hur BDD skiljer sig från TDD.
Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

## Frontend

För frontend-delen ska du börja med att beskriva existerande funktionalitet som funktionella krav. Dessa ska du skriva ner som user stories i STORIES.md. Sedan ska du skriva feature-filer för varje story och step-filer.

--- 

## Detta ska du göra

Skapa ett projekt, på det sättet vi gått igenom i kursen. Lägg till Git och ladda upp projektet till ett publikt repo på GitHub.
Skapa filerna README.md, STORIES.md och ANSWERS.md i projektets rotmapp.
Skriv backend-kod med TDD: enhetstest och integrationstest
Svara på teorifrågorna i filen ANSWERS.md
Formulera user stories för den funktionalitet som finns på webbsidan idag. Skriv ner dessa i STORIES.md.
Ta fram feature-filer utifrån dina user stories.
Bygg step-filer för alla features. Page-filer vid behov.
Implementera CI för projektet, så att alla dina tester körs när man pushar main-branchen till GitHub. (headless browser)
Skriv ner i README.md: 1) vad du har testat, och 2) hur man startar projektet. Nu kan du lämna in!

## Inlämning

Använd PyCharm eller VS Code för att skapa en textfil med namnet "exam_mitt_namn.txt" som innehåller länk till ditt projekt på GitHub. (Om du kompletterar ska filen heta "komplettering_mitt_namn.txt".) Denna textfil ska du lämna in på Teams. Kom ihåg att göra ditt projekt publikt. Skriv gärna om du har arbetat med bara G-krav eller även VG-kraven.

**Kontrollera noga innan du lämnar in. Felaktig inlämning kan leda till retur.**

--- 

## För G krävs

- Det finns enhetstester och integrationstester för BookStore och FavoriteBooks.
- Det finns user stories som täcker all funktionalitet i vyerna Katalog, Lägg till bok samt Mina böcker.
- Alla user stories har minst en feature. Alla features har minst ett scenario. Alla steg implementeras i någon step-fil.
- Det går att starta ditt projekt, med hjälp av instruktionerna du har skrivit i README.md.
- Alla test är gröna.

## För VG krävs

- Högre kvalitet och kod som återanvänds.
- User stories som täcker in vyn Statistik.
- Du använder designmönstret Page Object.
- Du använder Scenario Outline.
- Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.


Exempel på meningsfulla möjligheter: testa inte bara att det går att favoritmarkera, utan att det går att ta bort en favoritmarkering, och vad som händer om man klickar fler än två gånger. Det handlar om att försöka testa heltäckande - snarare än att göra enskilda stickprov.

---

## Tips
Flera element på sidan har ett test-id som du kan använda med Playwright.
Använd headless när du kommit en bit och när du lämnar in uppgiften. Det snabbar upp testandet rejält.
Kom ihåg att testa navigeringen också, inte bara innehållet i vyerna.
Rekommenderad mappstruktur för projektet: 08_playwright_bdd 



