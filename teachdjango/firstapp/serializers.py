from rest_framework import serializers

from teachdjango.firstapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name')