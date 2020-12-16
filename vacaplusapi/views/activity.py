"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vacaplusapi.models import Activity


class Activites(ViewSet):
    """Rare categories"""

    def create(self, request):
        """Handle activity operations for categories"""

        activity = Activity()

        activity.label = request.data["label"]

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
        activites = Activity.objects.all()

        serializer = ActivitySerializer(
            activites, many=True, context={'request': request})
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

        activity = Activity.objects.get(pk=pk)
        activity.label = request.data["label"]
        activity.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


"""Basic Serializer for single activity"""
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'description', 'date', 'photo', 'location')



