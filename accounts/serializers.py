from rest_framework import serializers
from .models import User
# import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = '__all__'
=======
        #fields = '__all__'
        fields = ['id', 'name', 'username', 'email', 'password']
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # all validated data except password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
>>>>>>> backend
