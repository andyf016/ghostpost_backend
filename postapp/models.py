from django.db import models
from django.utils import timezone

class Post(models.Model):
    CHOICES = (('b', 'Boast'), ('r', 'Roast'))
    sentiment = models.CharField(max_length=10, choices=CHOICES, default='b')
    body = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

