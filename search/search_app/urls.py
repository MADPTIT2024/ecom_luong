from django.urls import path
from . import views

urlpatterns = [
    path('<str:type_product>s/search', views.ProductSearchAPIView.as_view(), name='product_search'),
]
