
from django.contrib import admin
from django.urls import path
from book.views import all_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', all_books)
]
