from django.db import models
from django.utils import timezone

# class Event(models.Model):
    #
    # event_title=models.CharField(max_length=50)
    # event_description=models.CharField(max_length=500)
    # date_active=models.DateField(default=timezone.now())
    # time_active=models.TimeField(default=timezone.now())
    #
    # def __str__(self):
    #     return self.event_title


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=140)
    dateCreated = models.TimeField(default=timezone.now)


    def __str__(self):
        return str(self.title)

