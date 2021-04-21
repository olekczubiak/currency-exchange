from django.urls import path
from .views import courses

urlpatterns = [
    path('', courses),
    path('course/', courses),
]
