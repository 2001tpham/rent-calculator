from django.urls import path
from . import views


app_name = 'rentsplit'
urlpatterns = [
    path('', views.index, name='index')
]
