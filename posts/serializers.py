from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions, serializers


class User_SignUp_Serializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    password_check = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', "email", "password", "password_check")
        extra_kwargs = {'password': {'write_only': True}}
        required = ('email',)

    def create(self, validated_data):
        password = validated_data["password"]
        password_check = validated_data.pop("password_check")
        if (password == password_check):
            user = User.objects.create(**validated_data)
            return {
                "username": user.username,
                "email": user.email
            }
        else:
            raise exceptions.NotAcceptable(
                detail="passwords must match")


class User_Login_Serializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {'password': {'write_only': True}}
        required = ('email',)

    def validate(self, attrs):

        password = attrs.get("password")
        email = attrs.get("email")

        user = None
        user = User.objects.filter(Q(email__iexact=email)).first()
        # raise an authentication failed error if a user with that username or email doesn't exist.
        if user is None:
            raise exceptions.AuthenticationFailed(
                detail="user does not exist!")
        else:
            # check if password matches
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }

            else:
                raise exceptions.AuthenticationFailed(
                    detail="Wrong password")