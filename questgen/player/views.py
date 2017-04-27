from django.shortcuts import render
from django.http import Http404
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
        pass
