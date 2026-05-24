Feature:
	Som en Användare,
	vill jag kunna favoritmarkera b;cker,
	så jag enklare kan hitta dem.

	Background:
		Given att jag 'r p[ hemsidan
		And att jag st[r p[ sidan katalog
	
	Scenario:
		When jag markerar en rad
		And klickar p[ hj'rtat till h;ger
		Then ska boken favoritmarkeras
