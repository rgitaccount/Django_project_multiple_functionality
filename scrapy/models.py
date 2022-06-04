from django.db import models


class GoodReads(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class NytBooks(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title

