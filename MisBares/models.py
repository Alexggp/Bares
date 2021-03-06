from django.conf import settings
from django.db import models
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
import datetime


class Bar_db(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)  
    street=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=4, decimal_places=2)
    litre=models.DecimalField(max_digits=4, decimal_places=2, default=0)
    tapa=models.BooleanField(default=False)
    latitude=models.DecimalField(max_digits=9, decimal_places=7)
    longitude=models.DecimalField(max_digits=9, decimal_places=7)
    description = models.TextField()
    
    def __unicode__(self):              
        return self.name
      
class UserExtended_db(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birthday=models.DateField()
    points=models.IntegerField(default=0)
    
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        today = datetime.datetime.now()
        filename = '{}/{}/{}/{}.{}'.format(today.strftime("%Y"),today.strftime("%m"),today.strftime("%d"),uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("images")



class BarImages_db(models.Model):
    bar = models.ForeignKey(Bar_db)
    image = models.ImageField(upload_to=path_and_rename)

    
class Rates_db(models.Model):
    bar = models.ForeignKey(Bar_db)
    points=models.IntegerField()
    
class Comments_db(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    author_name=models.CharField(max_length=30)  
    bar = models.ForeignKey(Bar_db)
    text = models.TextField()
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    
#40.2868591, -3.8208389
#40.2874319, -3.8234138
#40.284191, -3.8216543 Cafeteria urjc
