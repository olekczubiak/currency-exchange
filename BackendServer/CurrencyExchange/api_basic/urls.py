from django.urls import path
from .views import CantorView


urlpatterns = [
    path('', CantorView.as_view()),
    path('cantor', CantorView.as_view()),
]
