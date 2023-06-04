from django.urls import path
from . import  views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_books', views.get_books_by_title_or_author, name='get_books_title_author'),
    path('save_favorite_book/<str:id_book>', views.save_favorite_book, name='save_favorite_book'),
    path('get_favorite_books', views.get_favorite_books, name='get_favorite_books'),
    path('delete_favorite_book/<str:id_book>', views.delete_favorite_book, name='delete_favorite_book'),
]