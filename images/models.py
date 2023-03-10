import uuid
from django.db import models
from django.conf import settings
from pathlib import Path
from .functions import path_to_upload_img

# get user model from settings
User = settings.AUTH_USER_MODEL


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(upload_to=path_to_upload_img, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)

    def get_filename(self):
        return Path(f'{self.image}').stem
    
    def __str__(self):
        return f'{self.get_filename()}'
    

class ThumbnailSize(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f'{self.width}x{self.height}'


class ExpiringLink(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.OneToOneField(Image, on_delete=models.CASCADE, unique=True)
    link = models.CharField(max_length=255)
    time_to_expired = models.IntegerField()

    def __str__(self):
        return f'{self.link}'