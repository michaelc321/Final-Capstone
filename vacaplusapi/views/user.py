"""View module for handling requests about rareusers"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action


class Users(ViewSet):
    """Users"""
    def list(self, request):
        """Handle GET requests to users resource
        Returns:
            Response -- JSON serialized list of users
        """
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Location

        Returns:
            Response -- JSON serialized Location
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
   
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for rareusers
    Arguments:
        serializers
    """
    class Meta:
        model = User
        fields = ('id','username', 'is_staff', 'is_active', 'first_name', 'last_name', 'email', 'date_joined')

