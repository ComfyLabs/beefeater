from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tenant
        fields = ('pk', 'user')
        extra_kwargs = {
            'pk': {'read_only': True},
        }

    def create(self, validated_data):
        user_serializer = UserSerializer()
        user = user_serializer.create(validated_data['user'])
        tenant = Tenant(user=user)
        tenant.save()
        return tenant
