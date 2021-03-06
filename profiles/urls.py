from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('delete_photo/<photo_id>', views.delete_photo, name='delete_photo'),
]
