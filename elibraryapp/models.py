from django.db import models

class Books(models.Model):
	book_file = models.FileField(upload_to='books_file', blank=True, null=True)
	title = models.CharField(max_length=100, blank=True, null=True)
	author = models.CharField(max_length=100, blank=True, null=True)
	about = models.TextField(blank=True, null=True)
	pages = models.CharField(max_length=5, blank=True, null=True)
	isbn = models.CharField(max_length=100, blank=True, null=True)
	cover_pic = models.ImageField(blank=True, null=True)

	def __str__(self):
		return str(self.title).title()

