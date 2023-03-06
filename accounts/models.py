from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from images.models import ThumbnailSize


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    account_tier = models.ForeignKey(
        'AccountTier',
        on_delete=models.SET_NULL,
        null=True
    )
    

class AccountTier(models.Model):
    name = models.CharField(max_length=64)
    thumbnail_size = models.ManyToManyField(ThumbnailSize, blank=True)
    is_expiring_link = models.BooleanField(
        default=False, 
        verbose_name='Expiring link')
    is_original_file = models.BooleanField(
        default=False,
        verbose_name='Original file')
