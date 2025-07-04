from django.db import models

class UserCredential(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)  # We'll keep it simple for now

    def __str__(self):
        return self.phone

class FishInventory(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    inventory = models.PositiveIntegerField()
    wholesale_price = models.FloatField()
    single_price = models.FloatField()

    def __str__(self):
        return f'{self.name} ({self.size})'
