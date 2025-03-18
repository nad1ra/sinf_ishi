from rest_framework import serializers
from .models import Product


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'comments']



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    desc = serializers.CharField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    created_at = serializers.DateTimeField()
