from django.contrib import admin
from .models import Show, Seat, Booking

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'price', 'available_seats')
    search_fields = ('title', 'location')
    list_filter = ('date',)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('show', 'row', 'number', 'is_booked')
    list_filter = ('show', 'is_booked')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'show', 'total_price', 'status', 'booking_time')
    list_filter = ('status', 'booking_time')
    search_fields = ('user__username', 'show__title') 