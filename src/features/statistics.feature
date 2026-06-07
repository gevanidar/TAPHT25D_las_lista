Feature:
	Som en Användare,
	vill jag kunna se statistik över antalet böcker och antalet favoritmarketade böcker 
	så jag kan vet hur många böcker som finns i katalogen och hur många av dem som är favoritmarkerade.

	Background:
		Given att jag är på hemsidan
	
	Scenario:
		When jag trycker på knappen statistics
 		Then ska jag se statistik för antal böcker Listan har 13 böcker.
		And  ska jag se statistik för antal favoritmarkerade böcker Våra användare har hjärtmarkerat 0 böcker. 

	Scenario:
		When jag trycker på knappen catalog
		And jag klickar på hjärtat
		And jag trycker på knappen statistics
 		Then ska jag se statistik för antal böcker 13
		And  ska jag se statistik för antal favoritmarkerade böcker 1

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titlen En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappen add-submit
		When jag trycker på knappen statistics
 		Then ska jag se statistik för antal böcker 14
		And  ska jag se statistik för antal favoritmarkerade böcker 0

	Scenario:
		When jag trycker på knappen catalog
		And jag klickar på hjärtat
		When jag trycker på knappen add-book
		And jag fyller i titlen En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappen add-submit
		And jag trycker på knappen statistics
 		Then ska jag se statistik för antal böcker 14
		And  ska jag se statistik för antal favoritmarkerade böcker 1

