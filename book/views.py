from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from datetime import datetime, timedelta
from django.views import generic


start_date = datetime.today() - timedelta(days=5)


class BooksListView(generic.ListView):
    template_name = "book/books.html"
    badge_classes = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
    queryset = models.Book.objects.order_by("id")
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genres = models.Genre.objects.all()
        context['badge_classes'] = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
        context['genres'] = genres
        return context


class BooksListViewByGenre(BooksListView):
    template_name = "book/books.html"
    paginate_by = 8

    def get_queryset(self, **kwargs):
        self.genre = get_object_or_404(models.Genre, name=self.kwargs['genre'])
        return models.Book.objects.filter(genre=self.genre)


class BookDetailView(generic.DetailView):
    template_name = "book/book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genres = models.Genre.objects.all()
        context['badge_classes'] = ["bg-success", "bg-primary", "bg-secondary", "bg-danger"]
        context['genres'] = genres
        return context


class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


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
