from rest_framework import generics

from ..serializers import UserSerializer


class UserRegistration(generics.CreateAPIView):
    """
    This is basically an API to create a user.
    This currently provides no email functionality.
    """
    serializer_class = UserSerializer
