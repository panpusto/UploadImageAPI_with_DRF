from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Image
from .utils import convert_to_thumbnails


@receiver(post_save, sender=Image)
def create_thumbnails(sender, instance: Image, **kwargs):
    convert_to_thumbnails(instance.id)
