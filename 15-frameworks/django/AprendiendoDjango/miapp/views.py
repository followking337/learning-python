import imp
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Model View Controller
# MTV = Model Template View

layout = """
    <h1>Sitio WEB con Django</h1>
    <hr>
    <ul>
        <li>
            <a href='/inicio'>Inicio</a>
        </li>
        <li>
            <a href='/hola-mundo'>Hola Mundo</a>
        </li>
        <li>
            <a href='/pagina-pruebas'>Página de pruebas</a>
        </li>
        <li>
            <a href='/contacto'>Contacto</a>
        </li>
    </ul>
    <hr>
"""


# def index(request):
#     html = """
#         <h2>Inicio</h2>
#         <p>Años hasta 2050:</p>
#         <ul>
#     """
#     year = 2021
#     while year <= 2050:
#         if year % 2 == 0:
#             html += f'<li>{year}</li>'
#         year += 1
#     html += '</ul>'
#     return HttpResponse(layout + html)


def index(request):
    nombre = 'Victor Robles'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']
    # lenguajes = []
    year = 2021
    hasta = range(year, 2051)
    return render(request, 'index.html', {
        'mi_variable': 'Soy un dato que esta en la vista',
        'title': 'Inicio 2',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    # html = HttpResponse(layout + """
    #     <h2>Hola Mundo con Django</h2>
    #     <h3>Soy Victor Robles WEB</h3>
    #     """)
    # return html
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
    elif redirigir == 2:
        return redirect('/contacto/Victor/')
    elif redirigir == 3:
        return redirect('contacto', nombre='Victor', apellidos='Robles')
    # return HttpResponse(layout + """
    #     <h2>Página de mi WEB</h2>
    #     <p>Creado por Victor Robles</p>
    # """)
    return render(request, 'pagina.html', {
        'texto': '',
        'texto2': 'soy texto2',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre='', apellidos=''):  # parámetros opcionales
    html = ''
    if nombre or apellidos:
        html += '<p>El nombre completo es:</p>'
        html += f'<h3>{nombre} {apellidos}</h3>'
    return HttpResponse(layout + '<h2>Contacto</h2>' + html)


# INSERT
def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )

    articulo.save()

    return HttpResponse(f'Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}')


def save_article(request):
    if request.method == 'GET':
        title = request.GET['title']
        if len(title) <= 5:
            return HttpResponse('<h2>El titulo es muy pequeño</h2>')
        content = request.GET['content']
        public = request.GET['public']
    elif request.method == 'POST':
        title = request.POST['title']
        if len(title) <= 5:
            return HttpResponse('<h2>El titulo es muy pequeño</h2>')
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f'Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}')
    else:
        return HttpResponse('<h2>No se ha podido crear el articulo</h2>')


def create_article(request):
    return render(request, 'create_article.html')


def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data  # for collecting data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            articulo = Article(
                title=title,
                content=content,
                public=public
            )
            articulo.save()
            # return HttpResponse(f'{articulo.title} - {articulo.content} - {articulo.public}')
            # Create flash message (one time per session)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')
            return redirect('articulos')
    else:
        formulario = FormArticle()
    return render(request, 'create_full_article.html', {'form': formulario})


# SELECT
def articulo(request):
    # articulo = Article.objects.get(pk=8)
    try:
        articulo = Article.objects.get(title='Superman', public=False)
        response = f'Articulo: <br/> {articulo.id} - {articulo.title}'
    except:
        response = '<h1>Articulo no encontrado</h1>'
    return HttpResponse(response)


# UPDATE
def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = 'Batman'
    articulo.content = 'Pelicula de 2017'
    articulo.public = True

    articulo.save()

    return HttpResponse(f'Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}')


# SELECT
def articulos(request):
    # articulos = Article.objects.all()
    articulos = Article.objects.filter(public=True).order_by('-id')
    # articulos = Article.objects.order_by('-title')[3:7]
    # articulos = Article.objects.filter(title='Batman', id=3)
    # articulos = Article.objects.filter(id__gte=10, title__contains='Articulo')
    # articulos = Article.objects.filter(title='Articulo',).exclude(public=False)
    # articulos = Article.objects.raw('SELECT * FROM miapp_article WHERE title="Articulo 2" and public=0')
    # articulos = Article.objects.filter(Q(title__contains=2) | Q(public=True))

    return render(request, 'articulos.html', {'articulos': articulos})


# DELETE
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')
