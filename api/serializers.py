from rest_framework import serializers
from .models import Notes, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notes
        fields = [
            "id",
            "user",
            "title",
            "text",
            "created_at",
            "updated_at"
        ]
        