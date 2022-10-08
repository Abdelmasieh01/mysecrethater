from django.urls import path
from .views import MessageViewset

urlpatterns = [
    path('home/', MessageViewset.ApiOverview, name='home'),
    path('send/', MessageViewset.SendMessage, name='send'),
    path('inbox/', MessageViewset.Inbox, name='inbox'),
    #path('users/', UserView.as_view(), name='users'),
]