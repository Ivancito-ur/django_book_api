from django.urls import path
from . import  views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_books', views.get_books_by_title_or_author, name='get_books_title_author')
]