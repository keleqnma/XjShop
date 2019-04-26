
import django_filters
from django.db.models import Q
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    过滤类
    """

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category__parent_category_id=value))
