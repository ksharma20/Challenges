from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):
    """Model definition for Quiz."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Quiz."""

        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizs'

    def __str__(self):
        """Unicode representation of Quiz."""
        return self.name


class Ques(models.Model):
    """Model definition for Ques."""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    ques = models.CharField(max_length=150)
    ans = models.CharField(max_length=150)
    user = models.ManyToManyField(User, null=True)

    class Meta:
        """Meta definition for Ques."""

        verbose_name = 'Ques'
        verbose_name_plural = 'Quess'

    def __str__(self):
        """Unicode representation of Ques."""
        return f"{self.ques} --> {self.quiz.name}"
