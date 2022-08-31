from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logreg.urls')),
    path('msgs/', include('msgs.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
