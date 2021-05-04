from rest_framework import serializers
from .models import Cantor


class CantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cantor
        fields = ['id', 'name', 'date', 'buy', 'sell', 'currency', 'website', 'rating',]


