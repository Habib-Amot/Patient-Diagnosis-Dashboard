from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# this models file contains the application own models as well as custome user model
# details regarding the application are stored in tables defined here


# defining the custom user manager object for the custom user model
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError("Email must be set for users")
        if not username:
            raise ValueError("Users Must Have a user name")
        user_model = self.model
        email = self.normalize_email(email=email)
        user = user_model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff") is True:
            raise ValueError("Super user must have 'is_staff' set to True")
        elif not extra_fields.get("is_superuser") is True:
            raise ValueError("Super user must have 'is_superuser' set to True")

        return self.create_user(email=email, username=username, password=password, **extra_fields)


# custom user model
class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

