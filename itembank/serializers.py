from django.forms import widgets
from rest_framework import serializers
from itembank.models import Itembank, Item

class ItembankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itembank
        fields = ('id', 'name', 'status')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'stem_text', 'itembank', 'status')
