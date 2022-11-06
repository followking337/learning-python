from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        return f'{self.first_name} {self.last_name}'


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Man'),
        (FEMALE, 'Woman')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        if self.gender == self.MALE:
            return f'Actor {self.first_name} {self.last_name}'
        else:
            return f'Actriz {self.first_name} {self.last_name}'


# from movie_app.models import Movie
class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles')
    ]
    # id --> will be created automatically by ORM
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    # any of these changes will affect DB structure, so makemigrations is required
    year = models.IntegerField(null=True, blank=True)  # allows null registers in this field
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(0)])  # default value if not set
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)  # default is only for new register
    slug = models.SlugField(default='', null=False, db_index=True)  # db_index -> searching in DB is faster
    # director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)  # one to many, cannot delete
    # director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)  # one to many, will delete
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    # g = Director.objects.all()[1]
    # g.movie_set.all()  --> field movie_set is creating automatically
    # director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)  # one to many, will set null
    actors = models.ManyToManyField(Actor)  # many to many, will delete, this field cannot be at list_display and edita

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        # return reverse('movie-detail', args=[self.id])
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        return f'{self.name} | {self.rating}%'
