from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from accounts.Serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content_data ={
                'provider_data':"Service Available",
                'message':'User created successfully',
                'status':200,
                'data':serializer.data,
                }
            return Response(content_data)
        else:
            content_data = {
                'provider_data':"Service Unavailable",
                'message':serializer.errors,
                'status':400,
                'data':serializer.data,
                }
            return Response(content_data)
                        
           