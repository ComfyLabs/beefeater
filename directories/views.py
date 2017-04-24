from rest_framework import generics

from .serializers import TenantSerializer


class TenantRegistration(generics.CreateAPIView):
    serializer_class = TenantSerializer
