from django.db import models
from django.contrib.auth.models import User
from rentsplit.models import ProfileAuth 
from datetime import date
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_message')
    profile = models.ForeignKey(ProfileAuth, on_delete=models.CASCADE, null=True, related_name='profile_message')
    subject = models.CharField(max_length=64)
    body = models.CharField(max_length=150)
    users_read = models.ManyToManyField(User, null=True, blank=True, related_name='read_message')
    created_date = models.DateField(default=timezone.now())
    replies = models.ForeignKey('Reply', on_delete=models.CASCADE, null=True, blank=True, related_name='reply_message')

    def format_date(self):
        return self.created_date.strftime('%m-%d-%Y')

    def __str__(self):
        return f'{self.sender}, {self.profile}'

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_reply')
    body = models.CharField(max_length=150)
    created_time = models.DateField(default=date.today().strftime('%m-%d-%Y'))
    parent_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message_reply')

# Create your models here.
