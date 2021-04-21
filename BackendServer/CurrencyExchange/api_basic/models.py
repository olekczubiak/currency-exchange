from django.db import models

class Cantor(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100)
    my_id = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    buy_EUR = models.CharField(max_length=100)
    sell_EUR = models.CharField(max_length=100)
    buy_GBP = models.CharField(max_length=100)
    sell_GBP = models.CharField(max_length=100)
    buy_CHF = models.CharField(max_length=100)
    sell_CHF = models.CharField(max_length=100)
    buy_USD = models.CharField(max_length=100)
    sell_USD = models.CharField(max_length=100)

    def __str__(self):
        return self.name
