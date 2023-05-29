from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=30)
    amt=models.IntegerField()

    def __str__(self):
        return self.pname