from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'review',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Testimonial, TestimonialAdmin)
