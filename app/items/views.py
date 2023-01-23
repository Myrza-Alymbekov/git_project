from django.shortcuts import render
from .models import Item
from rest_framework import viewsets, generics
from serializers import ItemSerializer


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

