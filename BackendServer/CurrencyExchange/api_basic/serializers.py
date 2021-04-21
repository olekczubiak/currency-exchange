from rest_framework import serializers
from .models import Cantor


class CantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cantor
        fields = ['name', 'date', 'website', 'my_id', 
                    'rating', 'buy_EUR', 'sell_EUR',
                            'buy_GBP', 'sell_GBP',
                            'buy_CHF', 'sell_CHF',
                            'buy_USD', 'sell_USD']
