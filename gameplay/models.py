from django.db import models
from django.conf import settings
from content.models import Quiz

class Attempt(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Reward(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badge = models.CharField(max_length=50, blank=True)
