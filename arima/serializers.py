from rest_framework import serializers
from .models import users



class usersSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields=['username','email','mobile']

