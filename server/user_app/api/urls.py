from django.urls import path
from . import views

urlpatterns = [
    path('auth', view=views.user_authentication),
    path('get-csrf-token', view=views.get_csrf_token)
]
