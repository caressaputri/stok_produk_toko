from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amount = models.IntegerField(default=0)


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
