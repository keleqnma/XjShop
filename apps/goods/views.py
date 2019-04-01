from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics
from .models import Goods
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

class GoodsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
   商品列表页,可以查看商品
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
