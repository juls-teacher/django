from django.db.models import Count, Sum
from rest_framework import viewsets

from rest_framework.generics import ListAPIView
from api.products.serializers import ProductModelSerializer, ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = (
        Product.objects.annotate(purchases_count=Count("purchases"))
        .annotate(purchases_total=Sum("purchases__count"))
        .order_by("-created_at")
    )
    serializer_class = ProductModelSerializer
    permission_classes = []


class TheMostExpensiveProductSet(ListAPIView):
    """
    the most expensive product
    """

    queryset = Product.objects.all().order_by("-price")
    serializer_class = ProductSerializer
    permission_classes = []


class TheMostPopularProductSet(ListAPIView):
    """
    The most popular product
    """

    queryset = Product.objects.annotate(
        purchases_total=Sum("purchases__count", default=0)
    ).order_by("-purchases_total")

    serializer_class = ProductSerializer
    permission_classes = []
