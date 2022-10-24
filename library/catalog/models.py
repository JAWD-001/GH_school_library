from django.db import models
from django.urls import reverse
import uuid 

# Create your models here.

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.name)

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=600, null=True)
    isbn = models.CharField('ISBN:', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)
    date_published = models.DateField(null=True, blank = True)
    publisher = models.CharField(max_length=200, null=True)
    language = models.ForeignKey('Language', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
    
class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    
    class Meta:
        ordering = ['due_date']
        
    def __str__(self):
        return f'{self.id} {self.book.id}'
        #return f'{self.id} {self.book.__str__()}'
        
#class User(models.Model):