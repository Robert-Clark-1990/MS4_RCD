from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),
]
