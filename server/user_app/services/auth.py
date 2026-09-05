from django.contrib.auth import authenticate, login as dj_login

class AuthenticationError(Exception):
    pass

def user_authentication_service(request, user_email, user_password):
    user = authenticate(request, username=user_email, password=user_password)
    if user is None:
        raise AuthenticationError
    else:
        dj_login(request=request, user=user)
        return user
    