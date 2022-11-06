from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


class RatingFilter(admin.SimpleListFilter):
    title = 'rating filter'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'low'),
            ('от 40 до 59', 'middle'),
            ('от 60 до 79', 'high'),
            ('>=80', 'top')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        elif self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']  # view fields in admin
    # exclude = ['slug']  # exclude these fields from viewing in admin
    # readonly_fields = ['year']  # field that cannot be changed in admin
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'year', 'budget', 'director', 'rating_status']
    # to view more other fields in admin
    # __str__ is not working after setting list_display
    # first field is link to that one specific register, so it can´t be editable
    list_editable = ['rating', 'year', 'director', 'budget']  # make fields editable from admin
    # filter_horizontal = ['actors']
    filter_vertical = ['actors']
    ordering = ['-rating', 'name']  # rating_status can't be used here because is not attribute
    list_per_page = 3
    actions = ['set_dollars', 'set_euro']  # register of the method
    # search_fields = ['name', 'rating']  # create search field in admin
    # search_fields = ['name__startswith', 'rating']  # __startswith -> search should begin from the left
    search_fields = ['name__istartswith', 'rating']  # __istartswith -> key sensitive (not working in sqlite)
    list_filter = ['name', 'currency', RatingFilter]  # create filters in admin

    @admin.display(ordering='rating', description='status')  # after decorating this field can be ordered
    def rating_status(self, movie: Movie):  # by default this field is can´t be ordered
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'Разок можно посмотреть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновлено {count_updated} записей', messages.ERROR)

# admin.site.register(Movie, MovieAdmin)  # same as decorator above
