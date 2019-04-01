from rest_framework import serializers
from .models import Goods,GoodsCategory

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category=CategorySerilizer()
    class Meta:
        model = Goods
        fields = "__all__"
