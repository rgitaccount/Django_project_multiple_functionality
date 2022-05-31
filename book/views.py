from django.shortcuts import render, get_object_or_404, redirect,reverse
from . import models, forms
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=5)


def all_books(request):
    books = models.Book.objects.all()
    genres = models.Genre.objects.all()
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    return render(request, "book/books.html", {"books": books,
                                               "badge_classes": badge_classes,
                                               "genres": genres})


def books_filtered_latest(request):
    queryset = models.Book.objects.filter(created_date__gt=start_date).order_by("-id")
    genres = models.Genre.objects.all()
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    return render(request, "book/books.html", {"books": queryset,
                                               "badge_classes": badge_classes,
                                               "genres": genres})


def books_filtered_by_name(request):
    queryset = models.Book.objects.order_by("title")
    genres = models.Genre.objects.all()
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    return render(request, "book/books.html", {"books": queryset,
                                               "badge_classes": badge_classes,
                                               "genres": genres})


def books_filtered_by_genre(request):
    q = request.GET.get('q')
    queryset = models.Book.objects.filter(genre__name=q)

    genres = models.Genre.objects.all()
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    return render(request, "book/books.html", {"books": queryset,
                                               "badge_classes": badge_classes,
                                               "genres": genres})


def book_detail(request, id):
    object = get_object_or_404(models.Book, id=id)
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    return render(request, "book/book_detail.html", {"book": object,
                                                     "badge_classes": badge_classes})


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


def update_book(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    method = request.method
    if method == "POST":
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books_url:books_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, "book/book_update.html", {"form": form, "object": book_object})


def delete_book(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return redirect(reverse("books_url:books_all"))
