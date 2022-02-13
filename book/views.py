from django.shortcuts import render
from . import models
from django.http import Http404
from django.shortcuts import get_object_or_404

def book_show_detail(request, id):
    try:
        book_show = get_object_or_404(models.book, id=id)
        try:
            comment = models.BookFeedBack.objects.filter(comment_id=id).\
                order_by("created_date")
        except models.book:
            print("No comments")
    except models.book:
        raise Http404("Book does not exist, try another id")
    return render(request, 'book_detail.html', {"book_show" : book_show, "comment" : comment })

def book_all(request):
    book = models.book.objects.all()
    return render(request, "book_list.html", {"book" : book})