from django.urls import path
from . import views

app_name = 'messageboard'
urlpatterns = [
    path('index/<str:profile_name>', views.index, name='index'),
    path('add-message/<str:profile_name>', views.add_message, name='add-message'),
]
