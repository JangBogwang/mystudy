from django.db import models

# Create your models here.
class Book(models.Model):
  book_name = models.CharField(primary_key = True, max_length = 30)
  author = models.CharField(max_length = 50)
  price = models.IntegerField()
  publisheddate = models.DateField()