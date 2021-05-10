from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
