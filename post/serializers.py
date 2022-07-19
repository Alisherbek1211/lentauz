from rest_framework import serializers
from .models import Post,Category,Company,Review


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = False, read_only = True)
    company = CompanySerializer(many = False, read_only = True)
    class Meta:
        model = Post
        fields = '__all__'