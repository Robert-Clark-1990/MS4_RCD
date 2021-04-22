from django.contrib import admin
from .models import ImageUpload


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'image',
        'comments'
    )


admin.site.register(ImageUpload, ImageUploadAdmin)
