from django.db import models
import datetime

# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.EmailField()
    lastEdit = models.DateTimeField(default=123456)

    def __str__(self):
        return self.title