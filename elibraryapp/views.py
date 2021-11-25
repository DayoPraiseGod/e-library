from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UploadBookForm
from .models import Books
from django.contrib import messages



def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'elibraryapp/register.html', context)

def login_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			# check if the user is superuser
			if user.is_superuser:
				login(request, user)
				return redirect('http://127.0.0.1:8000/admin/')
			elif user.is_staff and not user.is_superuser:
				login(request, user)
				return redirect('admin')
			elif user.is_active and not (user.is_superuser or user.is_staff):
				login(request, user)
				return redirect('booklist')

	return render(request, 'elibraryapp/login_page.html')

def logout_page(request):
	logout(request)
	return redirect('login')

@login_required
def booklist(request):
	books = Books.objects.all().order_by('-id')
	print(books[0].book_file.path)
	context = {'books':books}
	return render(request, 'elibraryapp/booklist.html', context)

@login_required
def admin_upload(request):
	form = UploadBookForm()
	if request.method == 'POST':
		form = UploadBookForm(request.POST, request.FILES)
		if form.is_valid:
			form.save()
			return redirect('booklist')
	context = {'form':form}
	return render(request, 'elibraryapp/admin.html', context)
