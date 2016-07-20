import copy

from rest_framework import serializers


class UserAuthSerializer(serializers.Serializer):
    auth = serializers.ChoiceField(['basic'])
    value = serializers.CharField()
