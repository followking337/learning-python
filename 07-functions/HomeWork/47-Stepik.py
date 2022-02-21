import datetime

print('\nЗадача 1')
adding_10 = lambda x: x + 10
print(adding_10(54))

print('\nЗадача 2.1')
starts_with = lambda s: s[0] == 'W'
print(starts_with('Wolf'))
print(starts_with('world'))
print(starts_with('camel'))

print('\nЗадача 2.2')
starts_with = lambda s: s.startswith('W')
print(starts_with('Wolf'))
print(starts_with('world'))
print(starts_with('camel'))

print('\nЗадача 3')
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

get_year = lambda now: now.year
get_month = lambda now: now.month
get_day = lambda now: now.day

print(get_day(now), get_month(now), get_year(now))
