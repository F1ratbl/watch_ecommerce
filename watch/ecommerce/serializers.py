from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Category, Product, ProductImage

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    display_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description',
            'brand', 'category',
            'price', 'discount_price', 'display_price',
            'stock', 'is_active', 'created_at', 'updated_at',
            'images'
        ]

    def get_display_price(self, obj):
        return obj.get_display_price()


