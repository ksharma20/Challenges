from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    """Model definition for Task."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """Unicode representation of Task."""
        return f"{self.name}  -->  {self.created_at}"
