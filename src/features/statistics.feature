Feature:
	Som en Användare,
	vill jag kunna se statistik över antalet böcker och antalet favoritmarketade böcker 
	så jag kan vet hur många böcker som finns i katalogen och hur många av dem som är favoritmarkerade.

	Background:
		Given att jag är på hemsidan
	
	Scenario:
		When jag trycker på knappen statistics
 		Then ska jag se statistik texten för antal böcker Listan har 13 böcker.
		And  ska jag se statistik texten för antal favoritmarkerade böcker Våra användare har hjärtmarkerat 0 böcker. 

	Scenario:
		When jag trycker på knappen favorites
		And jag klickar på hjärtat
		And jag trycker på knappen statistics
 		Then ska jag se statistik texten för antal böcker Listan har 13 böcker.
		And  ska jag se statistik texten för antal favoritmarkerade böcker Våra användare har hjärtmarkerat 1 böcker. 

	Scenario:
		When jag trycker på knappen add-bok
		And jag fyller i titeln En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappend add-submit
		When jag trycker på knappen statistics
 		Then ska jag se statistik texten för antal böcker Listan har 14 böcker.
		And  ska jag se statistik texten för antal favoritmarkerade böcker Våra användare har hjärtmarkerat 0 böcker. 

	Scenario:
		When jag trycker på knappen favorites
		And jag klickar på hjärtat
		When jag trycker på knappen add-bok
		And jag fyller i titeln En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappend add-submit
		And jag trycker på knappen statistics
 		Then ska jag se statistik texten för antal böcker Listan har 14 böcker.
		And  ska jag se statistik texten för antal favoritmarkerade böcker Våra användare har hjärtmarkerat 1 böcker. 

