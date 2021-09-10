from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

default_users = [
    User(name="Emmanuel Debrah", email="debrah@gmail.com"),
    User(name="Bismark Debrah", email="bismark@gmail.com"),
]


class LoginView(APIView):
    """
    Login API View
    Dummy login logic
    """
    def post(self, request):
        return Response(default_users[0].__dict__, status=status.HTTP_200_OK)

