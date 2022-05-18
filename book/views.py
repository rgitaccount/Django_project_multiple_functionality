from django.shortcuts import render, get_object_or_404
from . import models


def all_books(request):
    books = models.Book.objects.all()
    return render(request, "books.html", {"books": books})


def book_detail(request, id):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": object})
