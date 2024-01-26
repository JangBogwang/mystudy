from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

#GET 요청이 오면 처리 
@api_view(['GET'])
def hello(request):
  return Response("Hello REST API")

from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def booksAPI(request):
  #GET 방식의 처리 - 조회를 요청하는 경우
  if request.method == 'GET':
    #테이블의 데이터를 전부 가져오기
    books = Book.objects.all()
    #출력하기 위해서 브라우저의 형식으로 데이터를 변환 
    serializer = BookSerializer(books, many = True)
    #출력 
    return Response(serializer.data)
  #POST 방식의 처리 - 삽입하는 경우 
  elif request.method == 'POST':
    #클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성 
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
    

@api_view(['GET'])
def oneBook(request,bid):
  #book 테이블에서 book_name 컬럼의 값이 bid 인 값을 찾아온다.  
  book = get_object_or_404(Book, book_name = book_name)
  #출력할 수 있도록 변환
  serializer = BookSerializer(book)
  return Response(serializer.data)