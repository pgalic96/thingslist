from django.db import models


# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.EmailField()

    def __str__(self):
        return self.title