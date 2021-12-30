from django.db import models
from django.contrib.auth.models import User
from Product.models import Product


# Create your models here.
class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f"/cart/"



class Orders(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    products = models.ManyToManyField(Product)
    address = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f"/orders/"
