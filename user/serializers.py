from rest_framework import serializers
from .models import User


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        if attrs["login"] == "admin":
            raise serializers.ValidationError({"login": "This login cant be created"})
        if attrs["password"] == "admin":
            raise serializers.ValidationError({"password": "Password is to easy"})
        if attrs["sex"].lower() not in ["man", "woman"]:
            raise serializers.ValidationError({"gender": "Man or Woman?"})
        return super(PlayerSerializer, self).validate(attrs)

    def to_representation(self, instance):
        return {"message": "Completed!"}