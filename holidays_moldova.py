from dateutil.easter import easter as get_easter
from datetime import date, timedelta


def get_holidays(year, locality='chisinau', calendar=2):
	# CODUL MUNCII AL REPUBLICII MOLDOVA
	# Articolul 111. Zilele de sărbătoare nelucrătoare

	# numele localitatii

	# calendar
	# EASTER_JULIAN = 1
	# EASTER_ORTHODOX = 2
	# EASTER_WESTERN = 3

	holidays = {
		# a) 1 ianuarie – Anul Nou;
		date(year, 1, 1),
		# b) 7 şi 8 ianuarie – Naşterea lui Isus Hristos (Crăciunul pe stil vechi);
		date(year, 1, 7),
		date(year, 1, 8),
		# c) 8 martie – Ziua internaţională a femeii;
		date(year, 3, 8),
		# f) 1 mai – Ziua internaţională a solidarităţii oamenilor muncii;
		date(year, 5, 1),
		# g) 9 mai – Ziua Victoriei şi a comemorării eroilor căzuţi pentru
		date(year, 5, 9),
		# # ziua copiilor
		# date(year, 6, 1),
		# h) 27 august – Ziua Independenţei;
		date(year, 8, 27),
		# i) 31 august – sărbătoarea „Limba noastră”;
		date(year, 8, 31),
		# i) 25 decembrie - Naşterea lui Isus Hristos (Crăciunul pe stil nou);
		date(year, 12, 25),
	}

	# d) prima şi a doua zi de Paşte conform calendarului bisericesc;
	easter = get_easter(year, 2)
	holidays.add(easter)
	holidays.add(easter + timedelta(days=1))
	# e) ziua de luni la o săptămînă după Paşte ( Paştele Blajinilor);
	holidays.add(easter + timedelta(days=8))

	# j) ziua Hramului bisericii din localitatea respectivă, declarată în modul stabilit de consiliul local al municipiului, oraşului, comunei, satului.
	if locality in ['chisinau', 'bender', 'briceni', 'floresti', 'rezina']:
		holidays.add(date(year, 10, 14))
	elif locality in ['balti', 'basarabiasca', 'donduseni', 'falesti', 'javgur']:
		holidays.add(date(year, 9, 22))
	elif locality == 'orhei':
		holidays.add(date(year, 11, 8))
	elif locality in ['ungheni', 'drochia', 'soroca', 'cimislia', 'telenesti']:
		holidays.add(date(year, 8, 28))
	elif locality == 'cahul':
		holidays.add(date(year, 11, 21))
	elif locality in ['ialoveni', 'leova', 'straseni']:
		holidays.add(date(year, 10, 27))

	return holidays


if __name__ == '__main__':
	today = date.today()
	m = get_holidays(today.year)
	print("\n".join([str(i) for i in m]))
