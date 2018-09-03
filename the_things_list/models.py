from django.db import models
from django.urls import reverse
from django.utils import timezone

"""
Database model of Things, more precisely announcements
"""


class Thing(models.Model):
    # Title of the announcement
    title = models.CharField(max_length=200)
    # Text of the announcement
    text = models.TextField()
    # Author, identified by the e-mail field
    author = models.EmailField()
    # last edit time, the announcements are sorted by this on the front page
    lastEdit = models.DateTimeField('Timestamp', default=timezone.now)
    # random token, used for editing announcements
    random_str = models.CharField(max_length=32, unique=True)

    def get_absolute_url(self):
        return reverse('the_things_list:thing-details',
                       kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
