from django.db import models

# Create your models here.


# from book_app.models import Book
class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.title} - ' \
               f'rating: {self.rating} - ' \
               f'{"popular" if self.is_best_selling else "not popular"} - ' \
               f'author: {self.author}'
