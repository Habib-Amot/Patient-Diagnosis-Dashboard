from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from ..services.auth import AuthenticationError, user_authentication_service


@api_view(["POST"])
def user_authentication(request):
    try:
        refresh_token, access_token, username = user_authentication_service(request, request.data)

        response = Response(data={
            "STATUS":"LOGIN SUCCESSFUL",
            "details":{
                "message": "user authenticated successfully",
                "access_token": str(access_token),
                "user": username
            }
        }, status=status.HTTP_200_OK)

        # storing the refresh token in the session as an httpOnly cookie
        response.set_cookie(
            key="refresh_token",
            value=str(refresh_token),
            httponly=True,
            secure=True,
            samesite="Lax"
        )
        return response
    
    except AuthenticationError:
        return Response(data={
            "STATUS": "LOGIN FAILED",
            "details":{
                "message": "invalid username or password"
            }}, status=status.HTTP_401_UNAUTHORIZED)
        