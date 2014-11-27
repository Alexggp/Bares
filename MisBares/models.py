from django.conf import settings
from django.db import models


class Bar_db(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)  
    street=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=4, decimal_places=2)
    litre=models.DecimalField(max_digits=4, decimal_places=2, default=0)
    tapa=models.BooleanField(default=False)
    latitude=models.DecimalField(max_digits=9, decimal_places=7)
    longitude=models.DecimalField(max_digits=9, decimal_places=7)
    
    def __str__(self):              
        return self.name
      
class MySpecialUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birthday=models.DateField()    
    points=models.IntegerField(default=0)
    

#40.2868591, -3.8208389
#40.2874319, -3.8234138
#40.284191, -3.8216543 Cafeteria urjc
