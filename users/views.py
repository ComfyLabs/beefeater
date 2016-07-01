from __future__ import unicode_literals

from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserAuthSerializer, UserSerializer


class UserAuthentication(APIView):

    def post(self, request, format=None):
        """
        This leverages the HTTP basic authentication middleware
        that exists for authenticating requests to the application.

        The difference lies in where the user data is coming from.
        This data will be a part of the request payload, probably as
        Base64 encoded data.
        """
        auth = BasicAuthentication()

        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        credentials = serializer.data['value']

        user = auth.authenticate_credentials(
            credentials['username'], credentials['password']
        )
        instance = user[0]
        serialized_user = UserSerializer(instance)
        user_data = serialized_user.data

        return Response({'user': serialized_user.data})
