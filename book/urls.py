from django.urls import path
from . import views, models

app_name = "book"
urlpatterns = [
    path("book/", views.BookListView.as_view(), name="book_list"),
    path("book/<int:id>/", views.BookDetailView.as_view() , name="book_detail") ,
    path("book/<int:id>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("book/<int:id>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("add-book/", views.BookCreateView.as_view(), name="add_book"),
]
