from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Goods

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

class GoodsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
   商品列表页,分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
