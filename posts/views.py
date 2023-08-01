from .serializers import User_Login_Serializer, User_SignUp_Serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics
# Create your views here.


class User_Login_Serializer_View(TokenObtainPairView):
    """
    Custom Access token View
    """
    serializer_class = User_Login_Serializer


class User_SignUp_Serializer_View(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_SignUp_Serializer
    permission_classes = (AllowAny,)
