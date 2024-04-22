from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, ClothListCreate, ClothRetrieveUpdateDestroy

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),

    path('cloths/', ClothListCreate.as_view(), name='cloth-list'),
    path('cloths/<int:pk>/', ClothRetrieveUpdateDestroy.as_view(), name='cloth-detail'),
]
