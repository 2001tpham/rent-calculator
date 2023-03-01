from django.urls import path
from . import views


app_name = 'rentsplit'
urlpatterns = [
    path('', views.index, name='index'),
    path('guest-create-profile', views.guest_create_profile, name='guest-create-profile')
]
