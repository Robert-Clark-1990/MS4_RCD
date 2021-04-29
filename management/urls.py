from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('order_history/', views.order_history, name='order_history'),
    path('view_uploads/', views.view_uploads, name='view_uploads'),
]
