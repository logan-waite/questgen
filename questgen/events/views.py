from events.models import Event
from events.serializers import EventSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class EventList(APIView):
    # authentication_classes = (TokenAuthentication)
    # permission_classes = (IsAuthenticated,)
    """
    GET: Get an event, based on the next section of story needed by the player
    """

    def get(self, request, format=None):
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
