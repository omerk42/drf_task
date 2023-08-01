from posts import views
from django.urls import path

urlpatterns = [
    path("login", views.User_Login_Serializer_View.as_view(), name="user-login"),
    path("signup", views.User_SignUp_Serializer_View.as_view(), name="user-signup")
]
