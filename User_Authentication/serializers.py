from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password_confirmation']
        extra_kwargs = {'password': {'write_only': True}, 'password_confirmation': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Password and password confirmation do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = CustomUser.objects.create_user(**validated_data)
        return user


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")

            data['user'] = user
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'address']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'address']

