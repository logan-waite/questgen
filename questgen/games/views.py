from django.shortcuts import render
from django.http import Http404
from games.serializer import GameSerializer, UserSerializer
from games.models import Game
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GameList(APIView):
    """
    GET: Return games associated with current user
    GET (/<game_id>): Return all users associated with game id
    PUT: Create new game
    """

    def get(self, request, format=None):
        pass

    def put(self, request, format=None):
        serializer = GameSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            game = serializer.validated_data
            game_model = Game(name=game["name"])
            game_model.user = user
            game_model.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        print("I'm here now!")
        serializer.save(user=self.request.user)
