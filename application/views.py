from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group
from rest_framework.permissions import DjangoModelPermissions
from .permissions import *
User = get_user_model()



class GetRole(generics.ListAPIView):
    queryset = Group
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = GroupSerializer
    pagination_class = None

    def get_queryset(self):
        return self.request.user.groups


class UserApiView(generics.ListCreateAPIView):
    model = User
    permission_classes = (IsAdmin, )
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = UserSerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = None


class CategoryCreateApiView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin | IsManager]


class CategoryApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdmin | IsManager]
    serializer_class = CategorySerializer


class DessertListApiView(generics.ListAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = (permissions.AllowAny, )


class DessertCreateApiView(generics.CreateAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = [IsAdmin | IsManager]


class DessertApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dessert.objects.all()
    permission_classes = [IsAdmin | IsManager]
    serializer_class = DessertSerializer


class ClientApiView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = ClientSerializer


class ClientApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = ClientSerializer


class PayApiView(generics.ListCreateAPIView):
    queryset = Pay.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = PaySerializer


class PayApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pay.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = PaySerializer


class OrderApiView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = OrderSerializer


class OrderApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = OrderSerializer


class OrderDetailApiView(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = OrderDetailSerializer


class OrderDetailApiViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    permission_classes = (IsAdmin, )
    serializer_class = OrderDetailSerializer
