from django.urls import path, include
from .views import UserView
from rest_framework import urls

app_name = 'authentication'

urlpatterns = [
    path('accounts/profile/', UserView.as_view()),

]
