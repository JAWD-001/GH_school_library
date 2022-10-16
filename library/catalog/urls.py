from django.urls import path, include
from . import views

app_name = 'catalogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.BookCreate.as_view(), name='create'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]

#check 7:36 of django udemy course 
# django.contrib.auth.urls includes:
#accounts/login/
#accounts/logout/
#accounts/password_change