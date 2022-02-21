import json

print('\nАнализ продаж (1)')
with open('manager_sales.json', 'r') as file:
    data = json.load(file)
# with open('manager_sales.json', 'w') as file:
#     json.dump(data, file, indent=4)
# Лучше пересмотреть вложенность через: stop on print(i) --> debug --> calculator --> evaluate
    d = {}
    for i in data:
        for j in i['cars']:
            key = i['manager']['first_name'] + ' ' + i['manager']['last_name']
            d[key] = d.get(key, 0) + j['price']
    # for key, value in d.items():
    #     print(key, value)
    print(*max(d.items(), key=lambda x: x[1]))

print('\nАнализ продаж (2)')
with open('manager_sales.json', 'r') as file:
    data = json.load(file)
    maximum = 0
    max_name = ''
    max_lastname = ''
    for i in data:
        name = i['manager']['first_name']
        lastname = i['manager']['last_name']
        total = 0
        for j in i['cars']:
            total += j['price']
        if total > maximum:
            maximum = total
            max_name = name
            max_lastname = lastname
    print(max_name, max_lastname, maximum)

print('\nАнализ продаж (3)')
with open('manager_sales.json', 'r') as file:
    data = json.load(file)
    d = {}
    for i in data:
        d[f'{i["manager"]["first_name"]} {i["manager"]["last_name"]}'] = sum([j['price'] for j in i['cars']])
    print(*sorted(d.items(), key=lambda x: -x[1])[0])

print('\nЗадача 2.1')
with open('group_people.json', 'r') as file:
    data = json.load(file)
    d = {}
    for i in data:
        count = 0
        key = i['id_group']
        for j in i['people']:
            if j['gender'] == 'Female' and j['year'] > 1977:
                count += 1  # count += j['gender'] == 'Female' and j['year'] > 1977
        d[key] = count
    print(*max(d.items(), key=lambda x: x[1]))

print('\nЗадача 2.2')
with open('group_people.json', 'r') as file:
    data = json.load(file)
    maximum = 0
    max_group = None
    for group in data:
        count = 0
        id_group = group['id_group']
        for person in group['people']:
            if person['gender'] == 'Female' and person['year'] > 1977:
                count += 1
        if count > maximum:
            maximum = count
            max_group = id_group
    print(max_group, maximum)

print('\nЗадача 3.1')
with open('Alphabet.json', 'r') as file:
    code = json.load(file)
    with open('Abracadabra.txt', 'r') as origen:
        data = origen.read().replace('\n\n', '\n')
        with open('Answer.txt', 'w') as destiny:
            for letter in data:
                destiny.write(code.get(letter, letter))
                print(code.get(letter, letter), end='')

print('\n\nЗадача 3.2')
with open("Alphabet.json") as encode, open("Abracadabra.txt") as text:
    key = json.load(encode)
    data = text.read()
    print(data.translate(data.maketrans(key)))
