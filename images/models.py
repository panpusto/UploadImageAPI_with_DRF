import uuid
from django.db import models
from django.conf import settings
from .functions import path_to_upload_img

# get user model from settings
User = settings.AUTH_USER_MODEL


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(upload_to=path_to_upload_img)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)


class ThumbnailSize(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class ExpiringLink(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.OneToOneField(Image, on_delete=models.CASCADE, unique=True)
    link = models.CharField(max_length=255)
    time_to_expired = models.IntegerField()