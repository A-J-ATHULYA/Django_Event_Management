from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    event_date = models.DateField()
    ticket_price = models.PositiveIntegerField()
    status = models.BooleanField(default=True)


class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    event_name = models.CharField(max_length=100)
    ticket_count = models.PositiveIntegerField()