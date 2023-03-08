from rest_framework import generics
from .serializers import ImageListSerializer, ImageCreateSerializer
from .models import Image



class ImageListAPIView(generics.ListAPIView):
    serializer_class = ImageListSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)
        

class ImageCreateAPIView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)