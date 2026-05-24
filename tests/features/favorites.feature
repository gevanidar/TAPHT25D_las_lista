Feature:
	Som en Användare,
	vill jag kunna favoritmarkera böcker,
	så jag enklare kan hitta dem.

	Background:
		Given att jag är på hemsidan
		And att jag står på sidan katalog
	
	Scenario:
		When jag markerar en rad
		And jag klickar på hjärtat
		Then ska boken favoritmarkeras
