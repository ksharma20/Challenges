from django.db import models

# Create your models here.
class machine(models.Model):

    name = models.CharField(max_length=50)
    dtype = models.CharField(max_length=50)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
