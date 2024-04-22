from django.urls import path
from .views import ShipmentListCreateAPIView, ShipmentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('shipments/', ShipmentListCreateAPIView.as_view(), name='shipment-list-create'),
    path('shipments/<int:pk>/', ShipmentRetrieveUpdateDestroyAPIView.as_view(), name='shipment-detail'),
]
