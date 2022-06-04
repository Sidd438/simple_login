from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CustomLoginAPIView(APIView):

    def post(self, request):
        if 'username' in request.data:
            if request.data.get('username') == "SUTT_admin":
                pass
            else:
                return Response("Wrong Username", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No Username Provided", status=status.HTTP_400_BAD_REQUEST)
        if 'password' in request.data:
            if request.data.get('password') == "1234567890":
                return Response("Logged In", status=status.HTTP_200_OK)
            else:
                return Response("Wrong password", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No password Provided", status=status.HTTP_400_BAD_REQUEST)
