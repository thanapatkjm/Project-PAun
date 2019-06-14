from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import refridgerator_display_system

class get_all_user(APIView):
    def post(self,request):
        print("11111111")
        print(request.data)
        return Response({"id":"0123","status":"OPEN"})
