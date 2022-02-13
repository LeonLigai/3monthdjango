from django.shortcuts import render
from . import models


def book_all(request):
    book = models.book.objects.all()
    return render(request, "book_list.html", {"book" : book})