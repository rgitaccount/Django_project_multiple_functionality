from django.urls import path
from .import views

app_name = "books_url"
urlpatterns = [
    path('', views.all_books, name="books_all"),
    path('books/', views.all_books, name="books_all"),
    path('book/<int:id>/', views.book_detail, name="book"),
    path('main', views.test_main, name="main"),
    path('add-book/', views.add_book, name="add_book")
]

