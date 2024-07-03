from django.shortcuts import render
from .serializer import *
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'User Register Succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def register_list(request):
    user = User.objects.all()
    serializer = UserList(user,many = True)
    return Response({'Payload':serializer.data},status=status.HTTP_200_OK)

