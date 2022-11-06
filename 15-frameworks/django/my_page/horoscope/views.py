from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass


# Create your views here.

# -Static URL-
def leo(request):
    return HttpResponse('Знак зодиака Лев')


def scorpio(request):
    return HttpResponse('Знак зодиака Скорпион')


# -Dynamic URL-
def get_info_about_sign_zodiac(request, sign):
    if sign == 'leo':
        return HttpResponse('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).')
    elif sign == 'scorpio':
        return HttpResponse('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).')
    elif sign == 'taurus':
        return HttpResponse('Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).')
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign}')


# -Path Converter- Конвертор Роутов (поиск роутов идет сверху вниз)
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

elements = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_info_about_16(request):
    return HttpResponse('This is 16')


def get_info_about_zodiac_http(request, sign: str):  # второй аргумент - аргумент из динамического url
    description = zodiac_dict.get(sign)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')  # status 200
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign}')  # status 404


def get_info_about_zodiac_render_static(request, sign: str):
    # response = render_to_string('horoscope/info_zodiac_static.html')
    # return HttpResponse(response)
    return render(request, 'horoscope/info_zodiac_static.html')


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_about_zodiac_render_dynamic(request, sign: str):
    description = zodiac_dict.get(sign)
    zodiacs = list(zodiac_dict)
    data = {
        'description': description,  # keys from dict are variables in DTL
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
        # 'sign': sign.title(),
        # 'sign': sign,
        # 'my_int': 111,
        # 'my_float': 111.7,
        # 'my_list': [1, 2, 3, 4, 5],
        # 'my_tuple': (1, 2, 3, 4, 5),
        # 'my_dict': {'name': 'Jack', 'age': 40},
        # 'my_class': Person('Will', 55),
        # 'value1': [],
        # 'value2': [0]
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


# -Redirect-
def get_info_about_zodiac_by_number(request, sign: int):
    zodiacs = list(zodiac_dict)
    if sign > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign}')
    name_zodiac = zodiacs[sign - 1]
    # return HttpResponseRedirect(f'/horoscope/{name_zodiac}')
    # return HttpResponseRedirect('https://stepik.org/course/104792/syllabus')
    # redirected_url = reverse('horoscope-name', args=(name_zodiac,))  # args --> упорядочная коллекция
    redirected_url = reverse('horoscope-name', args=[name_zodiac])   # args --> упорядочная коллекция
    return HttpResponseRedirect(redirected_url)


# -Index-
def index_http(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirected_path = reverse('horoscope-name-render-dynamic', args=[sign])
        li_elements += f'<li> <a href="{redirected_path}">{sign.title()}</a> </li>'
    # response = '<br>'.join(zodiacs)
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def index_render(request):
    zodiacs = list(zodiac_dict)
    data = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
        'my_dict': {}
    }
    return render(request, 'horoscope/index.html', context=data)


# horoscope/type/
def type_index(request):
    li_elements = ''
    for element in list(elements):
        redirected_path = reverse('horoscope-type', args=[element])
        li_elements += f'<li> <a href="{redirected_path}">{element.title()}</a> </li>'
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)


# horoscope/type/<str:element>
def element_index(request, element: str):
    li_elements = ''
    for sign in elements.get(element):
        redirected_path = reverse('horoscope-name', args=[sign])
        li_elements += f'<li> <a href="{redirected_path}">{sign.title()}</a> </li>'
        # li_elements += f'<li> <a">{sign.title()}</a> </li>'
    response = f"""
            <ul>
                {li_elements}
            </ul>
            """
    return HttpResponse(response)
