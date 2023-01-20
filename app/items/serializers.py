from rest_framework import serializers
from app.items.models import Item


class ItemSerializer(serializers.Serializer):
    fields = '__all__'

    class Meta:
        model = Item
        