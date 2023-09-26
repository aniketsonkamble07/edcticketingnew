from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    location = models.CharField(max_length=200)    

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

class Participant(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participants')
    booking_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    participant_class = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    college = models.CharField(max_length=200)

class Booking(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
