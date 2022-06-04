from django.contrib import admin
from .models import Book, Author, Genre, Rating, BookFeedBack, BooksUser

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(BookFeedBack)
admin.site.register(BooksUser)
