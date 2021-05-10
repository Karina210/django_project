from rest_framework import serializers
from home.models import Product, Project


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'count', 'comment')


class ProjectSerislizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'difficulty', 'started_at', 'finished_at')
