from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers
from rest_framework.authtoken import views as _views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logreg.urls')),
    path('msgs/', include('msgs.urls')),

    path('api/', include('api.urls')),
    path('api-overview/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', _views.obtain_auth_token, name='auth-token'),
]
