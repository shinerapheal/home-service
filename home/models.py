from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Login_view(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
class Work(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    charge = models.IntegerField()


    def __str__(self):
        return self.name


class users(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Worker(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE, related_name='worker')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customers(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
class customer_info(models.Model):
    city=models.CharField(max_length=25,default='kochi')
class ac_info(models.Model):
    service=models.CharField(max_length=25)
class fridge_info(models.Model):
    service=models.CharField(max_length=25)
class user_in(models.Model):
    email=models.EmailField(max_length=25)
class conf(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    contact=models.IntegerField()
    item=models.CharField(max_length=25)
    service=models.CharField(max_length=25)
    adresee=models.TextField(max_length=500)
    sta=models.BooleanField(default=False)
    wor=models.CharField(max_length=50,default='no data')
    crea=models.DateTimeField(auto_now_add=True)

    
class woekstatus(models.Model):
    status=models.CharField(max_length=50)



    
