# Generated by Django 4.0.4 on 2022-06-04 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_rating_book_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookFeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_feedback', to='book.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_user', to='book.booksuser')),
            ],
        ),
    ]
