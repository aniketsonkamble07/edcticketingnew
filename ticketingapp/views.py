from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Ticket, Participant, Booking
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings


class BookingForm(forms.Form):
   
    quantity = forms.IntegerField(min_value=1)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=20)
    participant_class = forms.CharField(max_length=50)
    branch = forms.CharField(max_length=100)
    college = forms.CharField(max_length=200)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    available_tickets = Ticket.objects.filter(event=event, quantity_available__gt=0)
    return render(request, 'event_detail.html', {'event': event, 'available_tickets': available_tickets})

@login_required
def book_ticket(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            
            quantity = form.cleaned_data['quantity']
            user = request.user

            ticket = Ticket.objects.get(event=event,  quantity_available__gt=0)
            if ticket.quantity_available >= quantity:
                booking = Booking.objects.create(user=user, event=event, quantity=1)
                Participant.objects.create(user=user, event=event, booking_date=booking.booking_date,
                                           name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                           mobile_number=form.cleaned_data['mobile_number'],
                                           participant_class=form.cleaned_data['participant_class'],
                                           branch=form.cleaned_data['branch'], college=form.cleaned_data['college'])
                ticket.quantity_available -= quantity
                ticket.save()
                # Send email to user
                # subject = 'Ticket Booking Confirmation'
                # message = f"Dear {user.username},\n\nYou have successfully booked {quantity} ticket(s) for the event '{event.title}'.\n\nThank you!"
                # print(message)
                # from_email = settings.DEFAULT_FROM_EMAIL
                # recipient_list = [form.cleaned_data['email']]
                # print(recipient_list, from_email)
                # send_mail(subject, message, from_email, recipient_list)



                messages.success(request, 'Ticket booked successfully!')
                return redirect('event_detail', event_id=event.id)
            else:
                messages.error(request, 'Sorry, the requested ticket quantity is not available.')

    else:
        form = BookingForm()
    return render(request, 'book_ticket.html', {'event': event, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user_profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'profile.html', {'bookings': bookings})

from django.contrib.auth.views import LoginView, LogoutView

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    template_name = 'logout.html'


# Participants List
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def participants_list(request):
    participants = Participant.objects.all()
    return render(request, 'participants_list.html', {'participants': participants})

@staff_member_required
# Event wise participants list
def event_participants_list(request, event_id):
    participants = Participant.objects.filter(event=event_id)
    return render(request, 'participants_list.html', {'participants': participants})

