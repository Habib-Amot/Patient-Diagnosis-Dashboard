from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm

from .models import UserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password')


class CustomUserModificationForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

