from rest_framework import serializers
from player.models import Player, LANGUAGE_CHOICES, STYLE_CHOICES

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["name", "story_counter", "game", "meter"]
