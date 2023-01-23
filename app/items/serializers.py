from rest_framework import serializers
from app.items.models import Item


class ItemDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['item']


class ItemSerializer(serializers.Serializer):
    fields = '__all__'

    class Meta:
        model = Item
        