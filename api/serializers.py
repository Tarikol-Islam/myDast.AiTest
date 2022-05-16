from .models import UserMessage
from rest_framework import serializers


class UserMessageSrializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = "__all__"
