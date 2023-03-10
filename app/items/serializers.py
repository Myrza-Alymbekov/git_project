from rest_framework import serializers
from app.items.models import Item


class ItemDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['name']


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    count = serializers.IntegerField()

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        return item


