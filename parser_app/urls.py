from django.urls import path
from . import views

app_name = "parser"
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name="parser"),
    path('film/', views.FilmListView.as_view(),name="film_list"),
    path('film/<int:id>/', views.FilmDetailView.as_view, name="film_detail")
]