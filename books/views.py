from django.shortcuts import render, redirect
# Create your views here.

ERROR_MESSAGE_FORM = "If you want to search for books you need the title or name of the author."

def index(request):
    return render(request, 'books/index.html', {})

def get_book(request):
    if not request.POST['search_title'] or not request.POST['search_author']:
        return render(request, 'books/index.html', {'error_form': ERROR_MESSAGE_FORM})
    
    return render(request, 'books/index.html', {})

def view_404(request, exception=None):
    # redirect to homepage books when access to web app
    return redirect('/books/')

