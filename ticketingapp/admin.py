from django.contrib import admin


# Register your models here.
from .models import Event, Ticket, Participant, Booking

admin.site.site_header = 'EDC Ticketing Admin'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'description', 'location')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'price', 'quantity_available')
    list_filter = ('event', 'price')
    search_fields = ('event', 'price')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'booking_date', 'name', 'email', 'mobile_number', 'participant_class', 'branch', 'college')
    list_filter = ('user', 'event', 'booking_date')
    search_fields = ('user', 'event', 'booking_date')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'ticket_type', 'quantity', 'booking_date')
    list_filter = ('user', 'event', 'ticket_type', 'booking_date')
    search_fields = ('user', 'event', 'ticket_type', 'booking_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)
