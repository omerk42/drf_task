from posts import views
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path("login", views.User_Login_Serializer_View.as_view(), name="user-login"),
    path("signup", views.User_SignUp_Serializer_View.as_view(), name="user-signup"),
    path("token/verify", TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
