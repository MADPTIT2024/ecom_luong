from django.urls import path
from .views import PaymentListCreateAPIView, PaymentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]
