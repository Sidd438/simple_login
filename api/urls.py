from django.urls import path, include
from .views import CustomLoginAPIView


urlpatterns = [
    path('', CustomLoginAPIView.as_view()),
]
