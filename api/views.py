from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BooksSerializer
from elibraryapp.models import Books


@api_view(['GET'])
def apiBooksList(request):
	books = Books.objects.all()
	serializer = BooksSerializer(books, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def apiBookView(request, pk):
	books = Books.objects.get(id=pk)
	serializer = BooksSerializer(books, many=False)
	return Response(serializer.data)
	


