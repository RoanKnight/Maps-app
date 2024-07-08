from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(APIView):
  def post(self, request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username or not password:
      return Response(
          data={"message": "Both username and password are required."},
          status=status.HTTP_400_BAD_REQUEST
      )

    if User.objects.filter(username=username).exists():
      return Response(
          data={"message": "Username already exists."},
          status=status.HTTP_400_BAD_REQUEST
      )

    user = User.objects.create_user(
        username=username, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response(data={"message": "User created successfully.", "token": token.key}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
  def post(self, request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
      return Response(
          data={"message": "Both username and password are required."},
          status=status.HTTP_400_BAD_REQUEST
      )

    user = authenticate(username=username, password=password)
    if user:
      token, _ = Token.objects.get_or_create(user=user)
      return Response(data={"message": "Login successful.", "token": token.key}, status=status.HTTP_200_OK)
    else:
      return Response(data={"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedAPIView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(data={"message": "This is a protected view."}, status=status.HTTP_200_OK)
