from django.contrib import admin
from .models import Show, Seat, Booking, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'time', 'location', 'price', 'available_seats')
    search_fields = ('title', 'location')
    list_filter = ('category', 'date')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('show', 'row', 'number', 'is_booked')
    list_filter = ('show', 'is_booked')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'show', 'total_price', 'status', 'booking_time')
    list_filter = ('status', 'booking_time')
    search_fields = ('user__username', 'show__title') 