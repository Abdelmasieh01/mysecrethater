from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MessageSerializer, Message, User, UserSerializer
# Create your views here.

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            {
                'error': True,
                'error_msg': serializer.error_messages,
            },
            status = status.HTTP_400_BAD_REQUEST
        )

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date')
    serializer_class = MessageSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

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
        username = request.POST.get('user', False)
        value = request.POST.get('value', False)
        user = User.objects.get(username=username)
        message = MessageSerializer.data(user=user, value=value)

        if Message.objects.filter(user=user, value=value).exists():
            raise serializers.ValidationError('This message is already sent.')
        
        if message.is_valid():
            message.save()
            return Response(data=message.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['GET'])
    @permission_classes([permissions.IsAuthenticated])
    def Inbox(request):
        user = request.user
        messages = Message.objects.filter(user=user)
        serializer = MessageSerializer(data=messages, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    


