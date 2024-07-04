from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('userlist/', register_list, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
