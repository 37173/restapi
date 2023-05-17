from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import *

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
        fields = ( "id", "username", "email", "first_name", "last_name", "password", )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( "id", "name",)


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ("id", "name", "category", "price", "image", "description",)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ( "id", "first_name", "last_name", "patronymic", "phone",)

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = ( "id", "name",)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( "id", "client", "date_create", "pay", "address", "status",)

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ( "id", "order", "product", "count", "total_sum",)

class CategoryAndProductSerializer(serializers.ModelSerializer):
    products = DessertSerializer(many=True)
    
    class Meta:
        model = Category
        fields = ( "id", "name", "products",)

# class ProfilesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "email", "username", "first_name", "last_name", "password")


# class PlatoonsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Platoon
#         fields = "__all__"


# class NewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = New
#         fields = "__all__"


# class ElementsSliderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ElementsSlider
#         fields = "__all__"


# class CategoriesForPagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoriesForPage
#         fields = "__all__"


# class PagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Page
#         fields = "__all__"


# class MaterialsDistanceEducationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaterialsDistanceEducation
#         fields = "__all__"


# class PlatoonsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Platoon
#         fields = "__all__"


# class CategoriesAndPagesSerializer(serializers.ModelSerializer):
#     pages = PagesSerializer(source='pages_set', many=True)

#     class Meta:
#         model = CategoriesForPage
#         fields = "__all__"
