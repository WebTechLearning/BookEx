from django.shortcuts import render_to_response
from django.shortcuts import render
from books.models import Book

# Create your views here.
def book(request):
    books = Book.objects.order_by('create_date')
    return render_to_response('books.html', locals())

def list_books(request):
    """
    for template testing
    """
    return render(request, 'books_list.html', locals())
