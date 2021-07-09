from django.urls import path

from . import views

urlpatterns = [
    path('', views.search),
    # path('posts/<int:pk>/', views.DataMapDetail.as_view()),
]