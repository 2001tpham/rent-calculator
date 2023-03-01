from django.urls import path
from . import views


app_name = 'rentsplit'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-profile', views.guest_create_profile, name='create-profile')
]
