from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import UserMessageSrializer
from .models import UserMessage
# Create your views here.
class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSrializer
