from django.contrib.auth import authenticate, login as dj_login
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import AuthenticationSerializer

class AuthenticationError(Exception):
    pass

def user_authentication_service(request, user_data):
    data = AuthenticationSerializer(data=user_data)

    if data.is_valid():
        user_email = data.validated_data['email']
        user_password = data.validated_data['password']

        user = authenticate(request=request, username=user_email, password=user_password)

        if user is None:
            raise AuthenticationError
        else:
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            return {
                "token": {
                    "refresh": str(refresh_token),
                    "access": str(access_token),
                },
                "user":user.username
            }
    raise AuthenticationError
    