from django.contrib import admin

from . import models

admin.site.register(models.book)
admin.site.register(models.BookFeedBack)