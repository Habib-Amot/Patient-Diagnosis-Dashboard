from typing import Any

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# this models file contains the application own models as well as custome user model
# details regarding the application are stored in tables defined here


# defining the custom user manager object for the custom user model
class UserManager(BaseUserManager):
    def create(self, **kwargs: Any) -> Any:
        return self.create_user(**kwargs)

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

    def __str__(self) -> str:
        return f"({self.username}) {self.email} "

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"



class PatientDiagnosisReadings(models.Model):
    month = models.CharField(max_length=15)
    year = models.SmallIntegerField()
    blood_pressure = models.JSONField()
    heart_rate = models.JSONField()
    respiratory_rate = models.JSONField()
    temperature = models.JSONField()

    patient = models.ForeignKey('PatientProfile', on_delete=models.SET_NULL, null=True, blank=True)



class PatientDiagnosisList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=100)

    patient = models.ForeignKey('PatientProfile', on_delete=models.SET_NULL, null=True, blank=True)


class PatientLabResult(models.Model):
    lab_result = models.CharField(max_length=300)

    patient = models.ForeignKey('PatientProfile', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.lab_result


class PatientProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=30)
    age = models.SmallIntegerField(null=False, blank=False)
    profile_picture = models.ImageField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=40)
    emergency_contact = models.CharField(max_length=40)
    insurance_type = models.CharField(max_length=100)

    @property
    def name(self):
        return self.user.name

