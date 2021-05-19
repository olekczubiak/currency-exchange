from django.urls import path
from .views import CantorView, Last12RecordView, index


urlpatterns = [
    path('last', Last12RecordView.as_view()),
    path('history', CantorView.as_view()),
    path('', index, name='index'),
]
