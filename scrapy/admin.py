from django.contrib import admin
from . import models


@admin.register(models.GoodReads)
class GoodReads(admin.ModelAdmin):
    list_display = ("title", "link")


@admin.register(models.NytBooks)
class NytBooks(admin.ModelAdmin):
    list_display = ("title", "link")

