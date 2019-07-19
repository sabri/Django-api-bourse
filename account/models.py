from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_countries.fields import CountryField


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(blank=True, null=True, max_length=120)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    prof = (
        ('Salarié', 'Salarié'),
        ('Libre', 'Libre'),
        ('Commerçant', 'Commerçant'),
        ("Home d'affaire", "Home d'affaire"),
    )
    professional = models.CharField(choices=prof,default=None, max_length=12)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=4)
    photo = models.ImageField(upload_to='uploads', blank=True)
    phone = models.IntegerField(default=None)
    cin = models.IntegerField(default=None)
