from django.urls import path
from .views import MessageViewset, UserView

urlpatterns = [
    path('home/', MessageViewset.ApiOverview, name='home'),
    path('send/', MessageViewset.SendMessage, name='send'),
    #path('users/', UserView.as_view(), name='users'),
]