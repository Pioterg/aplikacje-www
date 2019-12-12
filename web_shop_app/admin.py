from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from web_shop_app.models import Klient, Zamowienie, Produkt

admin.site.register(Zamowienie)
admin.site.register(Produkt)


class KlientAdmin(UserAdmin):
    model = Klient
    list_display = ("login", "email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("login", "email", "password", "name", "surname")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "login",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    ordering = ("login",)


admin.site.register(Klient, KlientAdmin)
