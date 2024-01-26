from django.urls import path
from .views import hello, booksAPI, oneBook

urlpatterns = [
  path("hello/",hello),
  path("books/",booksAPI),
  path("book/<str:book_name>",oneBook)
]