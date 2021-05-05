from django.db import models

class Cantor(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    buy = models.FloatField(max_length=10)
    sell = models.FloatField(max_length=10) 
    currency = models.CharField(max_length=5)
    website = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
