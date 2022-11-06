from django.contrib import admin
from .models import Article, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):  # class to view registers in admin
    readonly_fields = ('created_at', 'updated_at')  # to view only reading fields in admin (created, updated)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#  Configurar el titulo del panel
admin.site.site_header = 'Master en Python - Victor Robles'
admin.site.site_title = 'Master'
admin.site.index_title = 'Panel de Gestion'
