# public legal holidays respublic of moldova

Only one dependency: `python-dateutil` use easter

## Conform
	CODUL MUNCII AL REPUBLICII MOLDOVA

	Articolul 111. Zilele de sărbătoare nelucrătoare

	[Art.111 al.(6) abrogat prin LP19 din 11.03.19, MO94-99/15.03.19 art.156; în vigoare 15.03.19]

# Use
```python
get_holidays(year=2024)
```
Return:
```python
[
	{
		"date": datetime.date(2024, 12, 25),
		"title": "Articolul 111, i) 25 decembrie - Naşterea lui Isus Hristos (Crăciunul pe stil nou)",
		"name": "Naşterea lui Isus Hristos (Crăciunul pe stil nou)"
	},
	# {...},
	# ...
]
```
