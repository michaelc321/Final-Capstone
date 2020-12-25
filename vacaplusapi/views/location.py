"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vacaplusapi.models import Location, VacaUser


class Locations(ViewSet):
    """Rare categories"""

    def create(self, request):
        """Handle Location operations for categories"""

        user = VacaUser.objects.get(user=request.auth.user)
        location = Location()

        location.time = request.data["time"]
        location.user = user
        location.title = request.data["title"]
        location.description = request.data["description"]
        location.photo = request.data["photo"]

        try:
            location.save()
            serializer = LocationSerializer(Location, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Location

        Returns:
            Response -- JSON serialized Location
        """
        try:
            location = Location.objects.get(pk=pk)
            serializer = LocationSerializer(location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Categories

        Returns:
            Response -- JSON serialized list of Categories
        """
        locations = Location.objects.all()

        serializer = LocationSerializer(
            locations, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Location
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            location = Location.objects.get(pk=pk)
            location.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for Categories"""

        location = Location.objects.get(pk=pk)
        location.time = request.data["time"]
        location.user = request.data["user"]
        location.title = request.data["title"]
        location.description = request.data["description"]
        location.photo = request.data["photo"]
        location.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


"""Basic Serializer for single Location"""
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'time', 'user', 'title', 'description', 'photo')



