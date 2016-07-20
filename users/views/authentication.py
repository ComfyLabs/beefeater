from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserAuthSerializer, UserSerializer
from ..auth_utils import decode_credentials


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

        encoded = serializer.data['value']
        credentials = decode_credentials(encoded)

        user = auth.authenticate_credentials(
            credentials['username'], credentials['password']
        )
        instance = user[0]
        serialized_user = UserSerializer(instance)

        return Response({'user': serialized_user.data})
