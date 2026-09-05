from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel
from .forms import CustomUserCreationForm, CustomUserModificationForm

# Register your models here.
class UserAdminCreation(UserAdmin):
    add_form = CustomUserCreationForm
    model = UserModel
    form = CustomUserModificationForm

    list_display = ['username', 'email', 'is_active']
    add_fieldsets = (
        (None, {
            'classes': 'wide',       
            'fields': ('email', 'username', 'password')
        }
        )
    )
    exclude = ['usable_password']

admin.site.register(UserModel, UserAdminCreation)
