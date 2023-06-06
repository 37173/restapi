from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView,
                                            TokenBlacklistView)

from .views import *

urlpatterns = [
    path('token/create/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('get-role/', GetRole.as_view()),
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>', UserApiViewUpdateDelete.as_view()),
    path('category/', CategoryListApiView.as_view()),
    path('category/create/', CategoryCreateApiView.as_view()),
    path('category/<int:pk>', CategoryApiViewUpdateDelete.as_view()),
    path('dessert/', DessertListApiView.as_view()),
    path('dessert/create/', DessertCreateApiView.as_view()),
    path('dessert/<int:pk>', DessertApiViewUpdateDelete.as_view()),
    path('client/', ClientApiView.as_view()),
    path('client/<int:pk>', ClientApiViewUpdateDelete.as_view()),
    path('pay/', PayApiView.as_view()),
    path('pay/<int:pk>', PayApiViewUpdateDelete.as_view()),
    path('order/', OrderApiView.as_view()),
    path('order/<int:pk>', OrderApiViewUpdateDelete.as_view()),
    path('order-detail/', OrderDetailApiView.as_view()),
    path('order-detail/<int:pk>', OrderDetailApiViewUpdateDelete.as_view()),
]
