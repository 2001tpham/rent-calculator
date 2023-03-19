from django.urls import path
from . import views

app_name = 'messageboard'
urlpatterns = [
    path('index/<str:profile_name>', views.index, name='index'),
    path('add-message/<str:profile_name>', views.add_message, name='add-message'),
    path('open-message/<str:profile_name>/<str:date>/<str:sender>/<str:subject>', views.open_message, name='open-message'),
    path('message-reply/<str:profile_name>/<str:date>/<str:sender>/<str:subject>', views.message_reply, name='message-reply'),
    path('delete-message/<str:profile_name>/<str:date>/<str:sender>/<str:subject>', views.delete_message, name='delete-message'),
]
