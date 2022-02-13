from django.urls import path
from . import views
urlpatterns = [
    path("book/<int:id>/", views.book_show_detail, name="book_detail") ,
    path("book/", views.book_all, name="book_list"),

]
