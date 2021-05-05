from django.urls import path
from .views import CantorView, Last12RecordView


urlpatterns = [
    path('', Last12RecordView.as_view()),
    path('history', CantorView.as_view()),
]
