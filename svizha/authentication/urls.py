from django.urls import path, include
from .views import UserView

app_name = 'authentication'

urlpatterns = [
    path('accounts/profile/', UserView.as_view()),

]
