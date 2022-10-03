from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers
from rest_framework.authtoken import views as _views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewset)

urlpatterns = [
    #Local app
    path('admin/', admin.site.urls),
    path('', include('logreg.urls')),
    path('msgs/', include('msgs.urls')),
    #rest_framework APIs
    path('api/', include('api.urls')),
    path('api-overview/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', _views.obtain_auth_token, name='auth-token'),
    #dj-rest-auth for authentication and registration
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
