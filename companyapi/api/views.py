from django.shortcuts import render
from rest_framework import viewsets
from api.models import company
from api.serializers import companyserializer

# Create your views here.
class companyviewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companyserializer