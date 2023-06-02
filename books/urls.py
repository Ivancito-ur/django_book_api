from django.urls import path
from . import  views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_book', views.get_book, name='get_book')
]