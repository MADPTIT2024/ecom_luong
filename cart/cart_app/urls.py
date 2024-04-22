from django.urls import path
from .views import GetCartAPIView,AddToCartAPIView, UpdateCartItemAPIView, RemoveCartItemAPIView,ViewCartAPIView,ListCartAPIView,RetrieveCartAPIView,CreateCartAPIView,UpdateCartAPIView,DeleteCartAPIView

urlpatterns = [
    path('carts/', ListCartAPIView.as_view(), name='list_carts'),
    path('view-carts/<int:user_id>/', GetCartAPIView.as_view(), name='view_cart'),
    path('carts/<int:pk>/', RetrieveCartAPIView.as_view(), name='retrieve_cart'),
    path('create-cart/', CreateCartAPIView.as_view(), name='create_cart'),
    path('update-cart/<int:pk>/', UpdateCartAPIView.as_view(), name='update_cart'),
    path('delete-cart/<int:pk>/', DeleteCartAPIView.as_view(), name='delete_cart'),
    path('add-to-cart/', AddToCartAPIView.as_view(), name='add_to_cart'),
    path('view-cart/<int:user_id>/', ViewCartAPIView.as_view(), name='view_cart'),
    path('update-cart-item/<int:pk>/', UpdateCartItemAPIView.as_view(), name='update_cart_item'),
    path('remove-cart-item/<int:pk>/', RemoveCartItemAPIView.as_view(), name='remove_cart_item'),
]