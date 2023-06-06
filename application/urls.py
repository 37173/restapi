from django.urls import path
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('get-role/', GetRole.as_view()),
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>', UserApiViewUpdateDelete.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('category/<int:pk>', CategoryApiViewUpdateDelete.as_view()),
    path('dessert/', DessertApiView.as_view()),
    path('dessert/<int:pk>', DessertApiViewUpdateDelete.as_view()),
    path('client/', ClientApiView.as_view()),
    path('client/<int:pk>', ClientApiViewUpdateDelete.as_view()),
    path('pay/', PayApiView.as_view()),
    path('pay/<int:pk>', PayApiViewUpdateDelete.as_view()),
    path('order/', OrderApiView.as_view()),
    path('order/<int:pk>', OrderApiViewUpdateDelete.as_view()),
    path('order-detail/', OrderDetailApiView.as_view()),
    path('order-detail/<int:pk>', OrderDetailApiViewUpdateDelete.as_view()),
    path('category-and-product/', CategoryAndProductApiView.as_view()),
]
