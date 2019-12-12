from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from web_shop_app.managers import UserManager


class Klient(AbstractBaseUser, PermissionsMixin):
    imie = models.CharField(max_length=254, blank=True, null=True)
    nazwisko = models.CharField(max_length=254, blank=True, null=True)
    login = models.CharField(unique=True, max_length=254, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.login


class Produkt(models.Model):
    nazwa = models.CharField(max_length=254, blank=False, null=False)
    opis = models.CharField(max_length=254, blank=True, null=True)
    cena = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)


class Zamowienie(models.Model):
    klient = models.ForeignKey(to=Klient, on_delete=models.CASCADE)
    produkt = models.ForeignKey(to=Produkt, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    ilosc = models.IntegerField(default=1)
