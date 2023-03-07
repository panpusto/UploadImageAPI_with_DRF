from django.contrib import admin
from .models import (
    Image,
    ThumbnailSize,
    ExpiringLink
)


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'user',
        'upload_date'
    )
    ordering = ['-upload_date']

admin.site.register(Image, ImageAdmin)
admin.site.register(ThumbnailSize)
admin.site.register(ExpiringLink)
