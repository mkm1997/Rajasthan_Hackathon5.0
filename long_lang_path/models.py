from django.db import models

# Create your models here.



class BusNo(models.Model):

    busno = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.busno



class Lat_Long(models.Model):
    busno = models.ForeignKey(BusNo,on_delete=models.CASCADE,blank=True,null=True)
    lat = models.CharField(max_length=100,blank=True)
    log = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.busno.busno)



