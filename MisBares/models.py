
from django.db import models


class Bar(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)  
    price=models.DecimalField(max_digits=4, decimal_places=2)
    latitude=models.DecimalField(max_digits=9, decimal_places=7)
    longitude=models.DecimalField(max_digits=9, decimal_places=7)
