from rest_framework import viewsets

from .models import Customer, Profession, DataSheet, Document
from .serializers import (
    CustomerSerializer,
    ProfessionSerializer,
    DataSheetSerializer,
    DocumentSerializer
)

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        active_customers = Customer.objects.filter(active=True)
        return active_customers


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer