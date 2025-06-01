from django_filters import rest_framework as filters

from tasks.models import Item


class ItemFilterSet(filters.FilterSet):
    """Item Filter Set"""

    ordering = filters.OrderingFilter(fields=("created",))

    class Meta:
        model = Item
        fields = {"status": ["exact"]}
