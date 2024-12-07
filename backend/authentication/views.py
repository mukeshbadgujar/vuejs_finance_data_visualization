from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer


class RegisterView(TokenObtainPairView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """Handles user login and provides access/refresh tokens."""
    
    serializer_class = CustomTokenObtainPairSerializer



class RefreshTokenView(TokenRefreshView):
    """Handles token refresh."""
    pass


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
        })
