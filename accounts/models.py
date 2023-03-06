from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
          default=uuid.uuid4,
            editable=False)
