from rest_framework import routers
from django.urls import path, include

from core.views import PostViews

router = routers.DefaultRouter()
router.register(r'posts', PostViews, basename='postsviews')

urlpatterns = [
    path('api/', include(router.urls)),
]
