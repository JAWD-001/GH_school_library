from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail=BookInstance.objects.filter(status='a').count()
    
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail,
    }
    
    return render(request,'catalog/index.html', context=context)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('login : book_detail')
    
class  BookDetail(DetailView):
    model = Book
    
    
