from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer, Message
# Create your views here.

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @api_view(['GET'])
    def ApiOverview(request):
        api_urls = {
            'all_items': '/',
            'Search by Category': '/?category=category_name',
            'Search by Subcategory': '/?subcategory=category_name',
            'Add': '/create',
            'Update': '/update/pk',
            'Delete': '/item/pk/delete'
        }
        return Response(api_urls)
    
    @api_view(['POST'])
    def SendMessage(request):
        message = MessageSerializer(data=request.data)

        if Message.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This message is already sent.')
        
        if message.is_valid():
            message.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    """ @api_vew(['GET'])
    def Inbox(request):
        message =  """
    


