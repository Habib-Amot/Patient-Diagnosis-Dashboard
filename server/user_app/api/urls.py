from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('auth', view=views.user_authentication),
    path('test', view=views.test_user_diagnosis_view),
    path('users', view=views.get_users),
    path('tokens/refresh', view=TokenRefreshView.as_view())
]
