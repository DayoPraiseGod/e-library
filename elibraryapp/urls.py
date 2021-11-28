from django.urls import path
from . import views

urlpatterns = [
	path('', views.login_page, name='login'),
	path('register/', views.register, name='register'),
	path('booklist/', views.booklist, name='booklist'),
	path('logout/', views.logout_page, name='logout'),
	path('read/', views.read, name='read'),
	path('admin_upload/', views.admin_upload, name='admin'),
	path('admin_upload/crud/', views.crud, name='crud'),
	path('admin_upload/crud/edit/<str:pk>/', views.edit, name='edit'),
	path('admin_upload/crud/delete/<str:pk>/', views.delete, name='delete'),
]