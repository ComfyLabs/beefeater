import copy

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .auth_utils import decode_credentials


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',)


class CredentialsSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAuthSerializer(serializers.Serializer):
    auth = serializers.ChoiceField(['basic'])
    value = CredentialsSerializer()

    def to_internal_value(self, data):
        username, password = decode_credentials(data['value'])
        decoded = {
            'username': username,
            'password': password,
        }

        _data = copy.deepcopy(data)
        _data['value'] = decoded

        return super(UserAuthSerializer, self).to_internal_value(_data)
