from django.shortcuts import render
from django.http import Http404
from player.serializer import PlayerSerializer
from games.models import Game
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PlayerList(APIView):
    """
    GET: Return the player name based on player_id
    PUT: Create new player
    """

    def get(self, request, format=None):
        pass

    def put(self, request, format=None):
        data = request.data
        game = Game.objects.get(user=request.user)
        data["game"] = game.id
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
