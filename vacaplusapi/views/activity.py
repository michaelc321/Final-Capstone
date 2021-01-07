"""View module for handling requests about categories"""
from vacaplusapi.models.vacauser import VacaUser
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vacaplusapi.models import Activity, Location


class Activities(ViewSet):
    """Rare categories"""

    def create(self, request):
        """Handle activity operations for categories"""

        activity = Activity()

        activity.name = request.data["name"]
        activity.description = request.data["description"]
        activity.date = request.data["date"]
        activity.photo = request.data["photo"]

        try:
            activity.save()
            serializer = ActivitySerializer(activity, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single activity

        Returns:
            Response -- JSON serialized activity
        """
        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(activity, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Categories

        Returns:
            Response -- JSON serialized list of Categories
        """

        # activity = VacaUser.objects.get(locationId=request.auth.user)
        activities = Activity.objects.all()

        serializer = ActivitySerializer(
            activities, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single activity
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            activity = Activity.objects.get(pk=pk)
            activity.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Activity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for Categories"""

        locationId = Location.objects.get(locationId=request.auth.user)
        activity = Activity()

        activity.name = request.data["name"]
        activity.description = request.data["description"]
        activity.date = request.data["date"]
        activity.photo = request.data["photo"]
        activity.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


"""Basic Serializer for single activity"""
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'date', 'photo')



