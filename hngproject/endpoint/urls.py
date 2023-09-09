from django.urls import path
from endpoint import views

urlpatterns = [
    path('api', views.get_info, name='get_info'),
]