from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics
from .models import Goods


class GoodsListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
   商品列表页
    """
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)