from django.urls import path
from .import views, models
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=5)


app_name = "books_url"
urlpatterns = [
    path('', views.BooksListView.as_view(), name="books_all"),
    path('books/', views.BooksListView.as_view(), name="books_all"),
    path('book/<int:id>/', views.BookDetailView.as_view(), name="book"),
    path('books/<str:genre>/', views.BooksListViewByGenre.as_view(), name="by_genre"),
    path('books/latest', views.BooksListView.as_view(
        queryset=models.Book.objects.filter(
            created_date__gt=start_date
        ).order_by("-id")
    ), name="latest"),
    path('books/by_name', views.BooksListView.as_view(
        queryset=models.Book.objects.order_by("title")), name="by_name"),


    # path('books/latest', views.books_filtered_latest, name="latest"),
    # path('books/by_name', views.books_filtered_by_name, name="by_name"),
    # path('books/by_genre', views.books_filtered_by_genre, name="by_genre"),
    path('add-book/', views.add_book, name="add_book"),
    path('books/<int:id>/update/', views.update_book, name="update_book"),
    path('books/<int:id>/delete/', views.delete_book, name="delete_book"),
]

