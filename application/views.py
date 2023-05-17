from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
User = get_user_model()

from .models import *
from .serializers import *

class UserApiView(generics.ListCreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer


class CategoryApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer


class DessertApiView(generics.ListCreateAPIView):
    queryset = Dessert.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DessertSerializer


class DessertApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dessert.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DessertSerializer


class ClientApiView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class ClientApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class PayApiView(generics.ListCreateAPIView):
    queryset = Pay.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaySerializer


class PayApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pay.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaySerializer

class OrderApiView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

class OrderApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

class OrderDetailApiView(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderDetailSerializer

class OrderDetailApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderDetailSerializer

class CategoryAndProductApiView(generics.GenericAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoryAndProductSerializer(categories, many=True)
        return Response(serializer.data)
    