from drf.librari.app import models
from django.contrib import admin

admin.site.register(models.Author)

admin.site.register(models.Project)
admin.site.register(models.ToDo)