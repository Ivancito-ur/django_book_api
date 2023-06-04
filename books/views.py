import requests, json
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from books.models.Book import Book


#Variables statics
ERROR_MESSAGE_FORM = "If you want to search for books you need the title or name of the author."
LINK_SEARCH_API_LIBRARY = "https://openlibrary.org/search.json?"
LINK_BOOK_API_LIBRARY = "https://openlibrary.org/books/"
LINK_API_LIBRARY = "https://openlibrary.org/"

def index(request):
    return render(request, 'books/index.html', {})


def get_books_by_title_or_author(request):
    """
    This method receives the title and name of the author to search through the GET 
    protocol. Verify that at least one of the two is 
    present, otherwise it returns an error to the initial page.
    Makes the request to the Open Library API and returns the most important values.

    Args:
        request (_type_): request from page

    Returns:
        books from API Open Library
    """
    there_is_at_least_one = request.GET['search_title'] or request.GET['search_author']
    
    if not there_is_at_least_one:
        return render(request, 'books/index.html', {'error_form': ERROR_MESSAGE_FORM})
    
    title_clear = str(request.GET['search_title']).strip().replace(" ","+")
    author_clear = str(request.GET['search_author']).strip().replace(" ","+")
    
    params = {'fields':'title, author_name, edition_count, edition_key, publisher, language, publish_date, seed, first_publish_year'}
    
    if title_clear and author_clear:
        request_api = requests.get(LINK_SEARCH_API_LIBRARY, params={'title': title_clear, 'author':author_clear} | params)
        
    elif title_clear:
        request_api = requests.get(LINK_SEARCH_API_LIBRARY, params={'title': title_clear} | params)
    
    else:
        request_api = requests.get(LINK_SEARCH_API_LIBRARY, params={'author':author_clear} | params)
        
    json_data = json.loads(request_api.text)
    
    return render(request, 'books/index.html', {'books':json_data['docs']})

def save_favorite_book(request, id_book):
    
    request_api = requests.get(LINK_BOOK_API_LIBRARY + id_book + ".json")
    json_data = json.loads(request_api.text)
    
    book = Book(
        id_book = id_book,
        title=json_data['title'], 
        link_access= LINK_API_LIBRARY + json_data['key'], 
        date_record=timezone.datetime.now()
    )
    
    book.save()
    
    return HttpResponseRedirect(reverse('books:get_favorite_books'))


def get_favorite_books(request):
    books = Book.objects.all()
    return render(request, 'books/favorites_group.html', {'books':books})


def delete_favorite_book(request, id_book):
    try:
        Book.objects.filter(id_book=id_book).delete()
    except:
        pass
    return HttpResponseRedirect(reverse('books:get_favorite_books'))
    

def view_404(request, exception=None):
    """
    Redirects to the main page if it fails due to a 404 error

    Args:
        request (_type_): use in the future
        exception (_type_, optional): Other acttions. Defaults to None.

    Returns:
        redirect books/
    """
    return redirect('/books/')

