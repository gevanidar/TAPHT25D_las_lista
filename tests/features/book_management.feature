Feature: Book management
	Som en användare
	Vill jag kunna lägga till bäcker
	Så jag kan utöka läslistan med de böcker jag läst

	Background:
		Given att jag är på hemsidan
		And att jag står på sidan katalog

	Scenario Outline:
		When jag trycker på knappen add-book
		And jag fyller i titeln <titel>
		And jag fyller i författaren <author>
		Then bör jag inte kunna trycka på knappen add-submit
		Examples:
			| titel | author |
			|  |  |
			| En bra bok |  |
			|  | En bra författare |

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		Then bör jag se en lista med 14 böcker
		And bör listan innehålla boken En bra bok och En bra författare

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappen add-submit
		And jag fyller i titeln En bättre bok
		And jag fyller i författaren En bättre författare
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		Then bör jag se en lista med 15 böcker
		And bör listan innehålla boken En bra bok och En bra författare
		And bör listan innehålla boken En bättre bok och En bättre författare
		And bör listans sista bok vara En bättre bok och En bättre författare

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln En bra bok
		And jag fyller i författaren En bra författare
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		And jag markerar en rad
		And jag klickar på hjärtat
		And jag trycker på knappen favorites
		Then ska jag se en bok med En bra bok i favoritlistan
