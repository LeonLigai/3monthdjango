from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path("book/", views.book_all, name="book_list"),
    path("book/<int:id>/", views.book_show_detail, name="book_detail") ,
    path("add-book/", views.add_book, name="add_book"),
]
