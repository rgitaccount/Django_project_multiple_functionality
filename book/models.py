from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)


class BooksUser(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class BookFeedBack(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_feedback")
    user = models.ForeignKey(BooksUser, on_delete=models.CASCADE, related_name="books_user", null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.books.title

