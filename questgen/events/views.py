from events.models import Event
from events.serializers import EventSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from events.generator import generateEvent

class EventList(APIView):

    """
    GET: Get an event, based on the next section of story needed by the player
    POST: Update player with results of event
    PUT: Create a new event
    """

    def get(self, request, format=None):
        event = generateEvent()
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

    def put(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
