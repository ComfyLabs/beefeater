import copy

from rest_framework import serializers

from .auth_utils import decode_credentials
from .serializers.common import UserSerializer


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
