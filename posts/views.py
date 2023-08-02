from .serializers import User_Login_Serializer, User_SignUp_Serializer, PostSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import Post
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
# Create your views here.


class User_Login_Serializer_View(TokenObtainPairView):
    serializer_class = User_Login_Serializer


class User_SignUp_Serializer_View(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_SignUp_Serializer
    permission_classes = (AllowAny,)


class Post_Create_View(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Post_Update_Delete_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
