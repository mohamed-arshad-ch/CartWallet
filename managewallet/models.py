from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    reff_code = models.CharField(max_length=100)
    refferd_user = models.CharField(max_length=150)

    def __str__(self):
        return self.reff_code


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    date_created = models.DateField(auto_now_add=True)
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    amount = models.IntegerField()
    buy_user = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
