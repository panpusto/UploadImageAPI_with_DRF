from rest_framework import serializers
from .models import Image


class ImageListSerializer(serializers.ModelSerializer):
    images = serializers.ListField(source='get_links')
    class Meta:
        model = Image
        fields = [
            'images'
        ]


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'image'
        ]
