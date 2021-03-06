from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'pk': {'read_only': True},
        }

    def create(self, validated_data):
        User = get_user_model()

        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
