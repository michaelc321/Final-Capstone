"""View module for handling requests about locationactivitys"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vacaplusapi.models import LocationActivity, Location, Activity, locationactivity

class LocationActivities(ViewSet):
    """Rare location activitys"""

    def list(self, request):
        """Handle GET requests to get locationactivitys by location"""

        locationactivities = LocationActivity.objects.all()

        #filtering locationactivitys by location
        location = self.request.query_params.get("location_id", None)

        if location is not None:
            locationactivities = locationactivities.filter(location_id=location)

        serializer = LocationActivitySerializer(
            locationactivities, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """Handle location operations"""

        location = Location.objects.get(pk=request.data["location_id"])
        activity = Activity.objects.get(pk=request.data["activity_id"])

        locationactivity = LocationActivity()
        locationactivity.location = location
        locationactivity.activity = activity

        try: 
            locationactivity.save()
            serializer = LocationActivitySerializer(locationactivity, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single locationactivity

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            locationactivity = LocationActivity.objects.get(pk=pk)
            locationactivity.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except LocationActivity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Location

        Returns:
            Response -- JSON serialized Location
        """
        try:
            locationactivity = LocationActivity.objects.get(pk=pk)
            serializer = LocationActivitySerializer(locationactivity, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        # try:
        #     location = Location.objects.get(pk=pk)
        #     activities = Activity.objects.filter(location=location)
        #     serializer = LocationSerializer(location, context={'request': request})
        #     return Response(serializer.data)
        # except Exception as ex:
        #     return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for Categories"""

        location = Location.objects.get(pk=request.data["location_id"])
        activity = Activity.objects.get(pk=request.data["activity_id"])

        locationactivity = LocationActivity()
        locationactivity.location = location
        locationactivity.activity = activity
        locationactivity.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for activitys"""
    class Meta:
        model = Activity
        fields = ('id', 'name')


class LocationActivitySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for locationactivitys"""

    activity = ActivitySerializer(many=False)

    class Meta:
        model = LocationActivity
        fields = ('id', 'location_id', 'activity_id', 'activity', 'location')
        depth = 1