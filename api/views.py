from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserMessageSerializer, UserSerializer
from .models import UserMessage
from rest_framework.authentication import TokenAuthentication
# Create your views here.

#for already Created User Generating the token
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
#That part was only for first time for created users who registered before the TokenAuthentication issue
    
#Views Part
from rest_framework.throttling import UserRateThrottle
from rest_framework import throttling

class PostUserRateThrottle(throttling.UserRateThrottle):
    scope = 'post_user'
    def allow_request(self, request, view):
        if request.method == "GET":
            return True
        return super().allow_request(request, view)


class UserMessageViewSet(viewsets.ModelViewSet):
    throttle_classes = [PostUserRateThrottle]
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(generics.ListAPIView):
  # throttle_classes = [UserRateThrottle]
  authentication_classes = [TokenAuthentication]
  permission_classes = (permissions.IsAuthenticated,)
  queryset = User.objects.all()
  serializer_class = UserSerializer


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = RegisterSerializer