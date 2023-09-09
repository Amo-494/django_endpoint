from django.urls import path
from endpoint import views

urlpatterns = [
    path('', views.get_info, name='get_info'),
]