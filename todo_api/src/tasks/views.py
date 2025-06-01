from rest_framework import viewsets

from tasks.filters import ItemFilterSet
from tasks.models import Item
from tasks.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Item View Set"""

    filterset_class = ItemFilterSet
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
