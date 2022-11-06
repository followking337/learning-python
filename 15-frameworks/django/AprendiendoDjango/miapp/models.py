from email.policy import default
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')  # verbose_name changes attribute name in admin
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Miniatura', upload_to='articles')
    public = models.BooleanField(verbose_name='¿Publicado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:  # change meta datos from DB table in admin
        verbose_name = 'Artículo'          # change singular name in admin
        verbose_name_plural = 'Artículos'  # change plural name in admin
        ordering = ['-id']                 # descending order in admin

    def __str__(self):
        if self.public:
            public = '(publicado)'
        else:
            public = '(no publicado)'
        return f'{self.title} {public}'


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
