from django.db import models

class book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=48)


class BookFeedBack(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(book, on_delete=models.CASCADE,
                                related_name="comment")