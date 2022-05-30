from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect,reverse
from . import models, forms


def all_books(request):
    books = models.Book.objects.all()
    return render(request, "book/books.html", {"books": books})


def book_detail(request, id):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "book/book_detail.html", {"book": object})


def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("books_url:books_all"))
    else:
        form = forms.BookForm()
    return render(request, "book/add_book.html", {"form": form})


def test_main(request):
    return render(request, "main.html")
