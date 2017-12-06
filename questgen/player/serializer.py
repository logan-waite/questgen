from rest_framework import serializers
from player.models import Player
from games.models import Game

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["name", "story_counter", "game", "meters"]
