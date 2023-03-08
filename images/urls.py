from django.urls import path
from .views import (
    ImageListAPIView,
    ImageCreateAPIView
)


urlpatterns = [
    path('upload', ImageCreateAPIView.as_view(), name='upload-image'),
    path('images/', ImageListAPIView.as_view(), name='image_list_api'),
]