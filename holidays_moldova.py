from dateutil.easter import easter as get_easter
from datetime import date, timedelta

def get_holidays_list(*args, **kwargs):
    holidays = get_holidays(*args, **kwargs)
    holidays_list = [i["date"] for i in holidays]
    return holidays_list

def get_holidays(year=date.today().year, locality='chisinau', calendar=2):
	"""Return dict of legal holydays in Moldova

	Keyword arguments:
	year -- the year of expecting, YYYY (default "curent year")
	locality -- the lity name, lowercase string (default chisinau)
	calendar -- int, EASTER_JULIAN = 1, EASTER_ORTHODOX = 2, EASTER_WESTERN = 3

	CODUL MUNCII AL REPUBLICII MOLDOVA
	Articolul 111. Zilele de sărbătoare nelucrătoare
	[Art.111 al.(6) abrogat prin LP19 din 11.03.19, MO94-99/15.03.19 art.156; în vigoare 15.03.19]
	"""

	holidays = [
		# a) 1 ianuarie - Anul Nou;
		{
			"date": date(year, 1, 1),
			"title": "Articolul 111, a) 1 ianuarie - Anul Nou",
			"name": "Anul Nou"
		},
		# b) 7 şi 8 ianuarie - Naşterea lui Isus Hristos (Crăciunul pe stil vechi);
		{
			"date": date(year, 1, 7),
			"title": "Articolul 111, b) 7 şi 8 ianuarie - Naşterea lui Isus Hristos (Crăciunul pe stil vechi)",
			"name": "Naşterea lui Isus Hristos"
		},
		{
			"date": date(year, 1, 8),
			"title": "Articolul 111, b) 7 şi 8 ianuarie - Naşterea lui Isus Hristos (Crăciunul pe stil vechi)",
			"name": "Naşterea lui Isus Hristos"
		},
		# c) 8 martie - Ziua internaţională a femeii;
		{
			"date": date(year, 3, 8),
			"title": "Articolul 111, 8 martie - Ziua internaţională a femeii",
			"name": "Ziua internaţională a femeii"
		},
		# f) 1 mai - Ziua internaţională a solidarităţii oamenilor muncii;
		{
			"date": date(year, 5, 1),
			"title": "Articolul 111, f) 1 mai - Ziua internaţională a solidarităţii oamenilor muncii",
			"name": "Ziua internaţională a solidarităţii oamenilor muncii"
		},
		# g) 9 mai - Ziua Victoriei şi a comemorării eroilor căzuţi pentru
		{
			"date": date(year, 5, 9),
			"title": "Articolul 111, g) 9 mai - Ziua Victoriei şi a comemorării eroilor căzuţi pentru independenţa Patriei, Ziua Europei",
			"name": "Ziua Victoriei şi a comemorării eroilor căzuţi pentru independenţa Patriei, Ziua Europei"
		},
		# h) 27 august - Ziua Independenţei;
		{
			"date": date(year, 8, 27),
			"title": "Articolul 111, h) 27 august - Ziua Independenţei",
			"name": "Ziua Independenţei"
		},
		# i) 31 august - sărbătoarea „Limba noastră”;
		{
			"date": date(year, 8, 31),
			"title": "Articolul 111, i) 31 august - sărbătoarea „Limba noastră”",
			"name": "sărbătoarea „Limba noastră”"
		},
		# i) 25 decembrie - Naşterea lui Isus Hristos (Crăciunul pe stil nou);
		{
			"date": date(year, 12, 25),
			"title": "Articolul 111, i) 25 decembrie - Naşterea lui Isus Hristos (Crăciunul pe stil nou)",
			"name": "Naşterea lui Isus Hristos (Crăciunul pe stil nou)"
		},
	]
	# d) prima şi a doua zi de Paşte conform calendarului bisericesc;
	easter = get_easter(year, calendar)
	holidays.append({
			"date": easter,
			"title": "Articolul 111, d) prima şi a doua zi de Paşte conform calendarului bisericesc",
			"name": "prima şi a doua zi de Paşte conform calendarului bisericesc"
	})
	holidays.append({
			"date": easter + timedelta(days=1),
			"title": "Articolul 111, d) prima şi a doua zi de Paşte conform calendarului bisericesc",
			"name": "prima şi a doua zi de Paşte conform calendarului bisericesc"
	})
	# e) ziua de luni la o săptămînă după Paşte ( Paştele Blajinilor);
	holidays.append({
			"date": easter + timedelta(days=8),
			"title": "Articolul 111, e) ziua de luni la o săptămînă după Paşte ( Paştele Blajinilor)",
			"name": "ziua de luni la o săptămînă după Paşte ( Paştele Blajinilor)"
	})
	# j) ziua Hramului bisericii din localitatea respectivă, declarată în modul stabilit de consiliul local al municipiului, oraşului, comunei, satului.
	hram = {
		"date": date(year, 10, 14),
		"title": "Articolul 111, j) ziua Hramului bisericii din localitatea respectivă, declarată în modul stabilit de consiliul local al municipiului, oraşului, comunei, satului",
		"name": f"ziua Hramului bisericii din localitatea „{locality.capitalize()}”"
	}
	if locality in ['tiraspol', 'chisinau', 'bender', 'briceni', 'floresti', 'rezina', 'dubasari']:
		hram["date"] = date(year, 10, 14)
		holidays.append(hram)
	elif locality in ['balti', 'basarabeasca', 'donduseni', 'falesti', 'javgur']:
		hram["date"] = date(year, 9, 22)
		holidays.append(hram)
	elif locality in ['ungheni', 'drochia', 'soroca', 'cimislia', 'telenesti']:
		hram["date"] = date(year, 8, 28)
		holidays.append(hram)
	elif locality in ['ialoveni', 'leova', 'straseni']:
		hram["date"] = date(year, 10, 27)
		holidays.append(hram)
	elif locality in ['edinet']:
		hram["date"] = date(year, 1, 14)
		holidays.append(hram)
	elif locality in ['comrat']:
		hram["date"] = date(year, 1, 20)
		holidays.append(hram)
	elif locality in ['ocnita', 'singerei', 'taraclia']:
		hram["date"] = date(year, 5, 6)
		holidays.append(hram)
	elif locality in ['riscani']:
		hram["date"] = date(year, 9, 21)
		holidays.append(hram)
	elif locality in ['calarasi']:
		hram["date"] = date(year, 6, 20)
		holidays.append(hram)
	elif locality in ['criuleni']:
		hram["date"] = date(year, 9, 20)
		holidays.append(hram)
	elif locality in ['causeni']:
		hram["date"] = date(year, 7, 12)
		holidays.append(hram)
	elif locality in ['stefan voda']:
		hram["date"] = date(year, 5, 30)
		holidays.append(hram)
	elif locality in ['anenii noi', 'cantemir', 'ceadir-lunga', 'orhei', 'cosnita']:
		hram["date"] = date(year, 11, 8)
		holidays.append(hram)
	elif locality in ['glodeni', 'cahul', 'hincesti', 'nisporeni', 'soldanesti', 'cainari', 'otac']:
		hram["date"] = date(year, 11, 21)
		holidays.append(hram)

	holidays.sort(key=lambda x: x["date"])
	return holidays


if __name__ == '__main__':
	holidays = get_holidays(year=date.today().year)
	print("\n".join([f"{str(i['date'])} - {i['name']}" for i in holidays]))
