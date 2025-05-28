from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.translation import gettext as _
from .managers import CustomUserManager
class CustomUser(AbstractUser):
   username = None
   email = models.EmailField(_('email address'),unique=True)
   number = models.IntegerField(blank=True)
   is_driver = models.BooleanField(default=False)
   is_ambulanceOrganizer_Person = models.BooleanField(default=False)
   is_Gov_Official = models.BooleanField(default=False)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   objects = CustomUserManager()

   def __str__(self):
        return self.email