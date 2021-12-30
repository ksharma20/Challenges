from django.db import models

# Create your models here.
class UData(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=50)
    description = models.CharField(default='', max_length=250)
    email = models.EmailField(max_length=254)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
