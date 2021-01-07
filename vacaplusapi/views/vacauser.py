"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vacaplusapi.models import VacaUser


class VacaUsers(ViewSet):
    """Rare categories"""

    def create(self, request):
        """Handle vacauser operations for categories"""

        vacauser = VacaUser()

        vacauser.user = request.data["user"]
        vacauser.bio = request.data["bio"]

        try:
            vacauser.save()
            serializer = VacaUserSerializer(vacauser, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single vacauser

        Returns:
            Response -- JSON serialized vacauser
        """
        try:
            vacauser = VacaUser.objects.get(pk=pk)
            serializer = VacaUserSerializer(vacauser, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Categories

        Returns:
            Response -- JSON serialized list of Categories
        """
        categories = VacaUser.objects.all()

        serializer = VacaUserSerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single vacauser
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            vacauser = VacaUser.objects.get(pk=pk)
            vacauser.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except VacaUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for Categories"""

        vacauser = VacaUser.objects.get(pk=pk)
        vacauser.label = request.data["label"]
        vacauser.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


"""Basic Serializer for single vacauser"""
class VacaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacaUser
        fields = ('id', 'user', 'bio')



