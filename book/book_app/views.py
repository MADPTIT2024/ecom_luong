from rest_framework import generics
from .models import Category, Author, Publisher, Book
from .serializers import CategorySerializer, AuthorSerializer, PublisherSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherListCreate(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProductSearchAPIView(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword', '')  # Lấy từ khóa từ tham số truy vấn
        if keyword:
            # Tìm kiếm sách theo tiêu đề hoặc mô tả chứa từ khóa
            books = Book.objects.filter(title__icontains=keyword) | Book.objects.filter(description__icontains=keyword)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Vui lòng cung cấp từ khóa để tìm kiếm.'}, status=400)