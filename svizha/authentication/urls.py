from django.urls import path, include
from .views import RegisterView, UserView, LogoutView, ChangePasswordView, DeleteAccountView
from rest_framework import urls

app_name = 'authentication'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('google-login/', GoogleLoginView.as_view()),
    # path('facebook-login/', FacebookLoginView.as_view()),
    path('accounts/profile/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('delete-account/', DeleteAccountView.as_view()),
    # path('confirm-email/<key>/', ConfirmEmailView.as_view()),

]
