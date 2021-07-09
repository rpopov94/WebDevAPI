from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import DataMapView

router = SimpleRouter()
router.register('api/map', DataMapView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]

urlpatterns += router.urls