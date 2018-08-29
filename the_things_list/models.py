from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.EmailField()
    lastEdit = models.DateTimeField('Timestamp', default=timezone.now)

    def get_absolute_url(self):
        return reverse('the_things_list:things-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
