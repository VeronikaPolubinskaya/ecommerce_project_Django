from django.contrib.auth.models import User
from rest_framework import serializers

from item.models import Item, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'