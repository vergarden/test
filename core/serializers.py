from rest_framework import serializers
from .models import BoardSaying, EmailSending


class BoardSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSaying
        fields = ['id', 'nickname', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']


class EmailSendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSending
        fields = ['id', 'name', 'email', 'subject', 'body', 'created_at']
        read_only_fields = ['id', 'created_at']
