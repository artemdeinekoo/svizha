from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.models import EmailConfirmation
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    """
    View for user regestration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# class GoogleLoginView(GoogleOAuth2Adapter.get_provider().get_login_view()):
#     pass
#
#
# class FacebookLoginView(FacebookOAuth2Adapter.get_provider().get_login_view()):
#     pass


# class TelegramLoginView(generics.CreateAPIView):
#     serializer_class = TelegramLoginSerializer
#     provider = TelegramOAuth2Provider


class UserView(generics.RetrieveAPIView):
    """
    View for getting a user.
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class LogoutView(APIView):
    """
    View for user logout.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.UpdateAPIView):
    """
    View for changing a password.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class DeleteAccountView(generics.DestroyAPIView):
    """
    View for deleting an account.
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ConfirmEmailView(APIView):
    """
    View for confirming an email.
    """
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        email_confirmation = get_object_or_404(EmailConfirmation, key=kwargs["key"])
        email_confirmation.confirm(self.request)
        return Response({'message': 'Email confirmed.'}, status=status.HTTP_200_OK)
