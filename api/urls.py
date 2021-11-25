from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiBooksList, name='books-list'),
	path('book-view/<str:pk>/', views.apiBookView, name='book-view'),
]