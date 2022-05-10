from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        #This is to not send the password for GET method
        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    # This is for having user created with hash entry
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


