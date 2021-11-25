from django.urls import path
from . import views

urlpatterns = [
	path('', views.login_page, name='login'),
	path('register/', views.register, name='register'),
	path('booklist/', views.booklist, name='booklist'),
	path('logout/', views.logout_page, name='logout'),
	path('admin_upload/', views.admin_upload, name='admin')
]