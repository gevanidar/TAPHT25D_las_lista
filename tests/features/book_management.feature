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
		And jag fyller i författaren <författare>
		Then bör jag inte kunna trycka på knappen add-submit
		Examples:
			| titel | författare |
			|  |  |
			| En bra bok |  |
			|   | En bra författare

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln <titel>
		And jag fyller i författaren <författare>
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		Then bör jag se en lista med 14 böcker
		And bör listan innehålla boken <titel> och <författare>

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln <titel>
		And jag fyller i författaren <författare>
		And jag trycker på knappen add-submit
		And jag fyller i titeln <titel2>
		And jag fyller i författaren <författare2>
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		Then bör jag se en lista med 15 böcker
		And bör listan innehålla boken <titel> och <författare>
		And bör listan innehålla boken <titel2> och <författare2>
		And bör listan innehålla boken <titel2> och <författare2> sist

	Scenario:
		When jag trycker på knappen add-book
		And jag fyller i titeln <titel>
		And jag fyller i författaren <författare>
		And jag trycker på knappen add-submit
		And jag trycker på knappen catalog
		And jag markerar en rad
		And jag klickar på hjärtat
		And jag trycker på knappen favorites
		Then ska jag se en bok med <titel> och <författare> i listan

