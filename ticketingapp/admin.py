from django.contrib import admin


# Register your models here.
from .models import Event, Ticket, Participant, Booking

admin.site.site_header = 'EDC Ticketing Admin'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'location')
    
    search_fields = ('title', 'description', 'location')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'price', 'quantity_available')
    list_filter = ('event', 'price')
    search_fields = ('event', 'price')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ( 'event', 'booking_date', 'name', 'email', 'mobile_number', 'participant_class', 'branch', 'college')
    list_filter = ( 'event', 'booking_date')
    search_fields = ( 'event', 'booking_date')

class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'event', 'ticket_type', 'quantity', 'booking_date')
    list_filter = ( 'event', 'ticket_type', 'booking_date')
    search_fields = ( 'event', 'ticket_type', 'booking_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)
