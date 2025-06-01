from rest_framework import serializers

from tasks.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Item Serializer"""

    class Meta:
        model = Item
        exclude = ["user"]
