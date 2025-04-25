from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from .models import Show, Seat, Booking
import json

class HomeView(View):
    def get(self, request):
        shows = Show.objects.filter(available_seats__gt=0).order_by('date', 'time')
        return render(request, 'booking/home.html', {'shows': shows})


class ShowDetailView(View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'booking/show_detail.html', {'show': show})


class BookTicketsView(LoginRequiredMixin, View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats = Seat.objects.filter(show=show).order_by('row', 'number')
        
        # Create seats if they don't exist for this show
        if not seats.exists():
            self._create_seats_for_show(show)
            seats = Seat.objects.filter(show=show).order_by('row', 'number')
        
        # Group seats by row for a better UI
        seat_rows = {}
        for seat in seats:
            if seat.row not in seat_rows:
                seat_rows[seat.row] = []
            seat_rows[seat.row].append(seat)
        
        return render(request, 'booking/book_tickets.html', {
            'show': show,
            'seat_rows': seat_rows
        })
    
    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        
        # Get the list of selected seat IDs
        selected_seat_ids = request.POST.getlist('seats')
        
        if not selected_seat_ids:
            messages.error(request, "Please select at least one seat.")
            return redirect('booking:book_tickets', show_id=show_id)
        
        try:
            # Attempt to book the seats
            with transaction.atomic():
                # Check if seats are still available
                selected_seats = Seat.objects.filter(id__in=selected_seat_ids, show=show, is_booked=False)
                
                if len(selected_seats) != len(selected_seat_ids):
                    messages.error(request, "Some selected seats are no longer available. Please try again.")
                    return redirect('booking:book_tickets', show_id=show_id)
                
                # Calculate total price
                total_price = show.price * len(selected_seats)
                
                # Create booking
                booking = Booking.objects.create(
                    user=request.user,
                    show=show,
                    total_price=total_price
                )
                
                # Add seats to the booking and mark them as booked
                for seat in selected_seats:
                    seat.is_booked = True
                    seat.save()
                    booking.seats.add(seat)
                
                # Update available seats count in the show
                show.available_seats -= len(selected_seats)
                show.save()
                
                return redirect('booking:booking_confirmation', booking_id=booking.id)
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('booking:book_tickets', show_id=show_id)
    
    def _create_seats_for_show(self, show):
        """Create seats for a show based on total_seats, organized in rows."""
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        seats_per_row = 10
        total_rows = (show.total_seats + seats_per_row - 1) // seats_per_row  # Ceiling division
        
        seats_to_create = []
        for row_idx in range(total_rows):
            row = rows[row_idx] if row_idx < len(rows) else f"R{row_idx+1}"
            for seat_num in range(1, seats_per_row + 1):
                # Don't exceed total seats
                if (row_idx * seats_per_row + seat_num) > show.total_seats:
                    break
                    
                seats_to_create.append(Seat(
                    show=show,
                    row=row,
                    number=seat_num,
                    is_booked=False
                ))
        
        Seat.objects.bulk_create(seats_to_create)


class BookingConfirmationView(LoginRequiredMixin, View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        return render(request, 'booking/booking_confirmation.html', {'booking': booking})


class BookingHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
        return render(request, 'booking/booking_history.html', {'bookings': bookings})
