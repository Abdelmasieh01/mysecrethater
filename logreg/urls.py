from django.urls import path
from . import views

app_name='logreg'

urlpatterns=[
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout')
]