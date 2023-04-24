from rest_framework import serializers
from .models import User


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:

        model = User

        fields = ['username', 'password', 'first_name','last_name']


    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
