from django.db import models

# Create your models here.
class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='')
    desc = models.CharField(max_length=500, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/product/{self.pk}/'