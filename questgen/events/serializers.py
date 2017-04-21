from rest_framework import serializers
from events.models import Event, LANGUAGE_CHOICES, STYLE_CHOICES

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_type", "choice", "story", "story_order")
