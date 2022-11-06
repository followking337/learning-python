from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def monday(request):
    return HttpResponse('нет дел')


def tuesday(request):
    return HttpResponse('сделать резюме')


week = {
    'monday': 'нет дел',
    'tuesday': 'сделать резюме',
    'wednesday': 'постирать',
    'thursday': 'поучить',
    'friday': 'сериал',
    'saturday': 'пробежка',
    'sunday': 'отдых'
}


def get_day_tasks(request, day: str):
    description = week.get(day)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Такого дня - {day} не существует')


def get_day(request, day: int):
    if 1 <= day <= 7:
        return HttpResponse(f'<h2>Сегодня {day} день недели </h2>')
    return HttpResponseNotFound(f'<h2>Неверный номер дня - {day} </h2>')


def get_day_redirected(request, day: int):
    if 1 <= day <= 7:
        week_day = list(week)
        # redirected_url = reverse('week_day', args=[week_day[day - 1]])
        # return HttpResponseRedirect(redirected_url)
        return HttpResponseRedirect(f'/todo_week/{week_day[day - 1]}')
    return HttpResponseNotFound(f'<h2>Неверный номер дня - {day} </h2>')


def index(request):
    return render(request, 'week_days/greeting.html')
