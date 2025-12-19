from django.db import models

# Create your models here.
class payment_form(models.Model):
    plan = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=16)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    expdate = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.plan}"