from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from web_shop_app.models import Klient, Zamowienie, Produkt
from web_shop_app.serializers import ZamowienieSerializer, ProduktSerializer, KlientSerializer


class Index(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {self.request.user}!"}, status=200)


class UtworzKlienta(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = KlientSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success!"})
        else:
            return Response({"message": "Fail!"})


class UtworzProdukt(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = ProduktSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "succcess"})
        else:
            return Response({"message": "fail"})


class UtworzZamowienie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = ZamowienieSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "succcess"})
        else:
            print(serializer.errors)
            return Response({"message": "fail"})


class KlienciView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"users": KlientSerializer(Klient.objects.all(), many=True).data},
        )


class ZamowieniaView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"orders": ZamowienieSerializer(Zamowienie.objects.all(), many=True).data},
        )


class ProduktyView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"comments": ProduktSerializer(Produkt.objects.all(), many=True).data},
        )
