# request_manager/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api1/', views.dummy_api1, name='dummy_api1'),
    path('api2/', views.dummy_api2, name='dummy_api2'),
]
