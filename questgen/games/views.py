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
        data = request.data
        print(request.user.id)
        data["user"] = request.user.pk
        print(data)
        serializer = GameSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
