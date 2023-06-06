from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ("id", "username", "email",
                  "first_name", "last_name", "password", )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ("id", "name", "category", "price", "image", "description",)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "patronymic", "phone",)


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = ("id", "name",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "client", "date_create", "pay", "address", "status",)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ("id", "order", "product", "count", "total_sum",)


class CategoryAndProductSerializer(serializers.ModelSerializer):
    products = DessertSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "products",)
