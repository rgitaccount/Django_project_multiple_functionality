from django.urls import path
from .import views


urlpatterns = [
    path('', views.all_books, name="books_all_url"),
    path('books/', views.all_books, name="books_all_url"),
    path('book/<int:id>/', views.book_detail, name="book_url")
]

