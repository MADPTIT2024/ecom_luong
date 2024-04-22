from rest_framework import generics
from .models import Category, Cloth
from .serializers import CategorySerializer, ClothSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ClothListCreate(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer

class ClothRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
