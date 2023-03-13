import uuid
import os
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
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

    def get_links(self):
        user_tier = self.user.account_tier
        base_file = os.path.dirname(self.image.name)
        thumbnails = default_storage.listdir(base_file)[1]
        localhost = 'http://localhost:8000'

        thumbs_for_user = []
        for thumbnail in thumbnails:
            if 'thumb' in thumbnail:
                thumbnails_path = os.path.join(base_file, thumbnail)
                thumbs_for_user.append(localhost + settings.MEDIA_URL + thumbnails_path)
            
        if user_tier.is_original_file:
            thumbs_for_user.append(localhost + self.image.url)

        if user_tier.is_expiring_link:
            pass
        # TODO: add after creating function to generate expiring links

        return thumbs_for_user


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