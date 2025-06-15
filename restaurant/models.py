from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    no_of_guests=models.IntegerField()
    bookingdate=models.DateField()

    def __str__(self):
        return self.name 

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title