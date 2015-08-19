from django.shortcuts import render_to_response
from books.models import Book

# Create your views here.
def book(request):
    books = Books.objects.order_by('create_date')
    return render_to_response('books.html', locals())
