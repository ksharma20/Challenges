from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class AuthUser(models.Model):

    user = models.OneToOneField(User, related_name="auth_user", on_delete=models.CASCADE)
    pnum = models.PositiveIntegerField( validators=[ MinLengthValidator(10), MaxLengthValidator(10) ] )
    ppic = models.ImageField(upload_to=f"{user}_pp.jpg", null=True, default="Default_PP.jpg")

    class Meta:
        verbose_name = "AuthUser"
        verbose_name_plural = "AuthUsers"

    def __str__(self):
        return self.user.fname

    def get_absolute_url(self):
        return reverse("AuthUser_detail", kwargs={"pk": self.pk})
