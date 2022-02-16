from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name='msgs'

urlpatterns = [
    path('send/<str:username>/', views.send, name='send'),
    path('my_msgs/', views.my_msgs, name='my_msgs'),
    path('fav/<int:message_id>/', views.fav, name='fav')
]

urlpatterns += staticfiles_urlpatterns()