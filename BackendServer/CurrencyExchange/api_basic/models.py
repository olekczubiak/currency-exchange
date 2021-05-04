from django.db import models

class Cantor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100, unique=True)
    rating = models.IntegerField(max_length=10)
    buy_EUR = models.FloatField(max_length=10)
    sell_EUR = models.FloatField(max_length=10)
    buy_GBP = models.FloatField(max_length=10)
    sell_GBP = models.FloatField(max_length=10)
    buy_CHF = models.FloatField(max_length=10)
    sell_CHF = models.FloatField(max_length=10)
    buy_USD = models.FloatField(max_length=10)
    sell_USD = models.FloatField(max_length=10)

    def __str__(self):
        return self.name
