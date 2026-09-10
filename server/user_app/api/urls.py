from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('auth', view=views.user_authentication),
    path('tokens/refresh', view=TokenRefreshView.as_view())
]
