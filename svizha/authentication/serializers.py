from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user authorization.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        """
        Method to check if passwords match up.
        """
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': "password field dont match !"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password1'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'])

        user.set_password(validated_data['password1'])

        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for getting a user.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'date_joined')
        read_only_fields = ('date_joined',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for changing a password.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'old_password', 'new_password')

    def update(self, instance, validated_data):
        """
        Method to check if user knows the old password and if he does, to update it in the database.
        """
        old_password = validated_data.pop('old_password', None)
        new_password = validated_data.pop('new_password', None)

        if not instance.check_password(old_password):
            raise serializers.ValidationError({'old_password': 'Wrong password'})

        instance.set_password(new_password)
        instance.save()
        return instance


class SocialSerializer(serializers.Serializer):
    """
    Serializer for social media authentication.
    """
    provider = serializers.CharField()
    access_token = serializers.CharField()

    def validate_provider(self, value):
        if value not in ["facebook", "google", "linkedin"]:
            raise serializers.ValidationError("Invalid provider")
        return value

    def validate_access_token(self, value):
        if not value:
            raise serializers.ValidationError("Access token cannot be empty")
        return value
