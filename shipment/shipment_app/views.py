from rest_framework import generics
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class ShipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
