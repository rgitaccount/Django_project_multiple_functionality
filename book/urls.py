from django.urls import path
from .import views

app_name = "books_url"
urlpatterns = [
    path('', views.all_books, name="books_all"),
    path('books/latest', views.books_filtered_latest, name="latest"),
    path('books/by_name', views.books_filtered_by_name, name="by_name"),
    path('books/by_genre', views.books_filtered_by_genre, name="by_genre"),
    path('books/', views.all_books, name="books_all"),
    path('book/<int:id>/', views.book_detail, name="book"),
    path('add-book/', views.add_book, name="add_book"),
    path('books/<int:id>/update/', views.update_book, name="update_book"),
    path('books/<int:id>/delete/', views.delete_book, name="delete_book"),
]

