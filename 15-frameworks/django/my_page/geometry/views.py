from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import math

# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    # return HttpResponse(f'<h2>Площадь прямоугольника размером {width}х{height} равна {area}</h2>')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    area = 2 * width
    # return HttpResponse(f'<h2>Площадь квадрата размером {width}х{width} равна {area}</h2>')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    area = 2 * math.pi * radius
    # return HttpResponse(f'<h2>Площадь круга с радиусом {radius} равна {area}</h2>')
    return render(request, 'geometry/circle.html')


def redirect(request, width=0, height=0, radius=0):  # "GET /calculate_geometry/get_rectangle_area/10/5 HTTP/1.1" 302 0
    redirected_url = ''
    if width != 0 and height != 0:
        redirected_url = reverse('rectangle', args=[width, height])
    elif width != 0 and height == 0:
        redirected_url = reverse('square', args=[width])
    elif radius != 0:
        redirected_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(redirected_url)
