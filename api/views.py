from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserMessageSerializer
from .models import UserMessage
# Create your views here.
class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
