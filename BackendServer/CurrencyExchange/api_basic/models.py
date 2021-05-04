from django.db import models

class Cantor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    buy = models.FloatField(max_length=10)
    sell = models.FloatField(max_length=10)
    currency = models.CharField(max_length=5)
    website = models.CharField(max_length=100, unique=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
