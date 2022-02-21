"""
JSON (JavaScript Object Notation) - текстовый формат обмена данными.
    JSON популярный формат предназначенный для обмена данными между сервером и клиентом
        либо сервером и другими серверами.

    JSON хранит данные в структурированном виде, походим на словарь.
    В Python есть стандартный модуль по работе с JSON. Название модуля - json

    loads(str_json): json str --> dict
    dumps(dict, indent=): dict --> json str
    dump(dict, file_json, indent=): dict --> json file
    load(file_json): json file --> dict

    Encoders and Decoders:
        JSON        Python
        object -->  dict
        array  -->  list
        string -->  str
        int    -->  int
        real   -->  float
        true   -->  True
        false  -->  False
        null   -->  None

    Формат файла json --> ctrl + alt + l
"""
import json
from random import randint
from datetime import datetime

print('\n1. json str --> dict:')
str_json = """
{
    "response": {
        "count": 5945964,
        "items": [{
            "first_name": "Денис",
            "id": 616635582,
            "last_name": "Мирошниченко",
            "can_access_closed": true
        }, {
            "first_name": "Ольга",
            "id": 499382437,
            "last_name": "Брюхачева",
            "can_access_closed": true
        }]
    }
}
"""
print(type(str_json))
data = json.loads(str_json)
print(data, type(data))
# print(data['response'])
# print(data['response']['count'])
# print(data['response']['items'])
# print(type(data['response']['items']))
for i in data['response']['items']:
    print(i['first_name'], i['last_name'])

print('\n2. Изменения Python объекта:')
for i in data['response']['items']:
    del i['id']
    i['likes'] = randint(100, 200)
    i['a'] = None
    i['now'] = datetime.now().strftime('%d-%m-%y')  # TypeError: Object of type datetime is not JSON serializable
print(data['response']['items'])

print('\n3.1 dict --> json str:')
new_json = json.dumps(data, indent=2)
print(new_json)  # русские буквы преобразовались к unicode

print('\n3.2 json str --> dict:')
print(json.loads(new_json))  # для того чтобы пересмотреть русский текст преобразовываем обратно к dict

print('\n4. dict --> json file:')
with open('my.json', 'w') as file:
    json.dump(data, file, indent=4)

print('\n5. json file --> dict:')
with open('my.json', 'r') as file:
    data = json.load(file)
print(data)
