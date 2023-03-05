from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class ProfileAuth(models.Model):
    name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(User, related_name='profile')
    rent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
    
class Expense(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_fr_user')
    amount = models.IntegerField(default=0)
    profile = models.ForeignKey(ProfileAuth, on_delete=models.CASCADE, null=True, related_name='expense_fr_profile')

    def __str__(self):
        return f'{self.name}, user:{self.user.username}, {self.amount}'