from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logreg.urls')),
    path('msgs/', include('msgs.urls')),
]
