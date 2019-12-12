"""app_www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web_shop_app.views import Index, UtworzKlienta, UtworzProdukt, UtworzZamowienie, KlienciView, ProduktyView, ZamowieniaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('klienci/utworz/', UtworzKlienta.as_view()),
    path('produkty/utworz/', UtworzProdukt.as_view()),
    path('zamowienia/utworz/', UtworzZamowienie.as_view()),
    path('zamowienia/', ZamowieniaView.as_view()),
    path('produkty/', ProduktyView.as_view()),
    path('klienci/', KlienciView.as_view()),
]
