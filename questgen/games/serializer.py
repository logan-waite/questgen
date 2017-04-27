from rest_framework import serializers
from games.models import Game
from django.contrib.auth.models import User

class GameSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Game
        fields = ["name", "user"]

class UserSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ["username", "games"]
