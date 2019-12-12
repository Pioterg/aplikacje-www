import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from web_shop_app.models import Produkt, Klient, Zamowienie


class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ["nazwa", "opis", "cena"]

    def validate_title(self, name):
        if not name:
            raise serializers.ValidationError("Name cannot be empty field")
        return name


class ZamowienieSerializer(serializers.ModelSerializer):
    produkt = serializers.SlugRelatedField(slug_field="nazwa", queryset=Produkt.objects.all())
    klient = serializers.SlugRelatedField(
        slug_field="login", queryset=Klient.objects.all()
    )

    class Meta:
        model = Zamowienie
        fields = ["klient", "produkt", "ilosc"]


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ["login", "imie", "nazwisko", "email", "password"]

    def validate_login(self, login):
        if not login or not login.isalpha():
            raise serializers.ValidationError("Login cannot be empty field")
        return login

    def validate_email(self, email):
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if not (re.search(regex, email)):
            raise serializers.ValidationError("Wrong email format!")
        else:
            return email

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(
                "Make sure your password is at lest 8 letters"
            )
        elif re.search("[0-9]", password) is None:
            raise serializers.ValidationError(
                "Make sure your password has a number in it"
            )
        else:
            return make_password(password)
