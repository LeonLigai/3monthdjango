from django.db import models

from django.db import models


class book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    author = models.CharField(max_length=48)
#hw2
class BookFeedback(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    book_comment = models.ForeignKey(Book_shop, on_delete=models.CASCADE,
                                     related_name="book_comment")