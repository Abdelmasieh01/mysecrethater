from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import messageSerializer, Message
# Create your views here.

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date')
    serializer_class = messageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

