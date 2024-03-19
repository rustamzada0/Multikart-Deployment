from rest_framework import serializers
from ..models import Subscriber


class SubsciberReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            "id",
            "email"
        )


class SubsciberCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            "id",
            "email"
        )