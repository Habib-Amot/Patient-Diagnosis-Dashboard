from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from ..services.auth import AuthenticationError, user_authentication_service


@api_view(["POST"])
def user_authentication(request):
    try:
        response = user_authentication_service(request, request.data)
        return Response(data={
            "STATUS":"LOGIN SUCCESSFUL",
            "details":{
                "message":response
            }
        }, status=status.HTTP_200_OK)
    
    except AuthenticationError:
        return Response(data={
            "STATUS": "LOGIN FAILED",
            "details":{
                "message": "invalid username or password"
            }}, status=status.HTTP_401_UNAUTHORIZED)
        