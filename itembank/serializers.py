from django.forms import widgets
from rest_framework import serializers
from itembank.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'status')

class ItembankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itembank
        fields = ('id', 'stem_text', 'itembank', 'status')