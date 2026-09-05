from django.http import JsonResponse
from django.middleware.csrf import get_token

from ..services.auth import AuthenticationError, user_authentication_service
from utils.parser import parse_json

def get_csrf_token(request):
    token = get_token(request)
    print(token)
    return JsonResponse({"value": token})


def user_authentication(request):
    if request.method == "POST":
        data = parse_json(request.body)
        user_email = data.get("email", None)
        user_password = data.get("password", None)
        print(user_email, user_password)
        
        try:
            user = user_authentication_service(request, user_email, user_password)
            return JsonResponse({
                "status":"SUCCESS",
                "detail": "Login successful".capitalize()
            })
        except AuthenticationError:
            return JsonResponse({
                "status": "INVALID CREDS",
                "detail":"please use a valid username or password".capitalize()
            })