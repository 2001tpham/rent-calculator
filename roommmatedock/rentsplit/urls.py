from django.urls import path
from . import views


app_name = 'rentsplit'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-profile', views.create_profile, name='create-profile'),
    path('user-profile/<str:profile_name>', views.user_profile, name='user-profile'),
    path('add-expense/<str:profile_name>', views.add_expense, name='add-expense'),
    path('update-rent/<str:profile_name>', views.update_rent, name='update-rent'),
    path('remove/<str:expense_name>/<str:profile_name>', views.remove_expense, name='remove-expense'),
    path('add-user/<str:profile_name>', views.add_user, name='add-user'),
    path('reset-profile/:<str:profile_name>', views.reset_profile, name='reset-profile'),
]
