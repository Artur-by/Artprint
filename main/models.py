from django.db import models

# Create your models here.
class Pricepillow(models.Model):
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    side = models.CharField(max_length=10)


class Colorpillow(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

class Sizepillow(models.Model):
    size = models.CharField(max_length=20)
    price = models.FloatField()

class Side(models.Model):
    side = models.CharField(max_length=20)
    price = models.FloatField()

#class Order(models.Model):
#   product = models.CharField(max_length=10)
