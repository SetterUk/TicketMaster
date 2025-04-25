from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from booking.models import Show, Booking
from django.db.models import Count, Sum
from datetime import datetime

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('adminpanel:login')


class AdminLoginView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('adminpanel:dashboard')
        return render(request, 'adminpanel/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminpanel:dashboard')
        else:
            messages.error(request, "Invalid credentials or insufficient permissions")
            return render(request, 'adminpanel/login.html')


class DashboardView(AdminRequiredMixin, View):
    def get(self, request):
        # Get basic statistics
        total_shows = Show.objects.count()
        total_bookings = Booking.objects.count()
        total_revenue = Booking.objects.filter(status='confirmed').aggregate(Sum('total_price'))['total_price__sum'] or 0
        
        # Get shows by date
        today = datetime.now().date()
        upcoming_shows = Show.objects.filter(date__gte=today).order_by('date')[:5]
        
        # Get recent bookings
        recent_bookings = Booking.objects.order_by('-booking_time')[:5]
        
        # Get shows with their booking counts
        popular_shows = Show.objects.annotate(booking_count=Count('bookings')).order_by('-booking_count')[:5]
        
        context = {
            'total_shows': total_shows,
            'total_bookings': total_bookings,
            'total_revenue': total_revenue,
            'upcoming_shows': upcoming_shows,
            'recent_bookings': recent_bookings,
            'popular_shows': popular_shows,
        }
        
        return render(request, 'adminpanel/dashboard.html', context)


class ShowListView(AdminRequiredMixin, View):
    def get(self, request):
        shows = Show.objects.all().order_by('date', 'time')
        return render(request, 'adminpanel/show_list.html', {'shows': shows})


class ShowCreateView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'adminpanel/show_form.html')
    
    def post(self, request):
        # Extract form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        price = request.POST.get('price')
        total_seats = request.POST.get('total_seats')
        image_url = request.POST.get('image_url', '')
        
        # Validation
        if not all([title, description, date, time, location, price, total_seats]):
            messages.error(request, "All fields are required")
            return render(request, 'adminpanel/show_form.html')
        
        try:
            # Create show
            show = Show.objects.create(
                title=title,
                description=description,
                date=date,
                time=time,
                location=location,
                price=price,
                total_seats=total_seats,
                available_seats=total_seats,
                image_url=image_url
            )
            messages.success(request, f"Show '{title}' created successfully!")
            return redirect('adminpanel:show_list')
        except Exception as e:
            messages.error(request, f"Error creating show: {str(e)}")
            return render(request, 'adminpanel/show_form.html')


class ShowUpdateView(AdminRequiredMixin, View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'adminpanel/show_form.html', {'show': show})
    
    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        
        # Extract form data
        show.title = request.POST.get('title')
        show.description = request.POST.get('description')
        show.date = request.POST.get('date')
        show.time = request.POST.get('time')
        show.location = request.POST.get('location')
        show.price = request.POST.get('price')
        
        # Handle total seats - can only increase, not decrease
        new_total_seats = int(request.POST.get('total_seats'))
        old_total_seats = show.total_seats
        
        if new_total_seats < old_total_seats:
            messages.error(request, "Total seats cannot be decreased once set")
            return render(request, 'adminpanel/show_form.html', {'show': show})
        
        # Update available seats if total increased
        if new_total_seats > old_total_seats:
            show.available_seats += (new_total_seats - old_total_seats)
        
        show.total_seats = new_total_seats
        show.image_url = request.POST.get('image_url', '')
        
        try:
            show.save()
            messages.success(request, f"Show '{show.title}' updated successfully!")
            return redirect('adminpanel:show_list')
        except Exception as e:
            messages.error(request, f"Error updating show: {str(e)}")
            return render(request, 'adminpanel/show_form.html', {'show': show})


class ShowDeleteView(AdminRequiredMixin, View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'adminpanel/show_form.html', {'show': show, 'confirm_delete': True})
    
    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        
        # Check if show has any bookings
        if show.bookings.exists():
            messages.error(request, "Cannot delete show with existing bookings")
            return redirect('adminpanel:show_list')
        
        try:
            show_title = show.title
            show.delete()
            messages.success(request, f"Show '{show_title}' deleted successfully!")
            return redirect('adminpanel:show_list')
        except Exception as e:
            messages.error(request, f"Error deleting show: {str(e)}")
            return redirect('adminpanel:show_list')


class BookingListView(AdminRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.all().order_by('-booking_time')
        return render(request, 'adminpanel/booking_list.html', {'bookings': bookings})
