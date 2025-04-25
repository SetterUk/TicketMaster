from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('show/<int:show_id>/', views.ShowDetailView.as_view(), name='show_detail'),
    path('book/<int:show_id>/', views.BookTicketsView.as_view(), name='book_tickets'),
    path('confirm/<int:booking_id>/', views.BookingConfirmationView.as_view(), name='booking_confirmation'),
    path('history/', views.BookingHistoryView.as_view(), name='booking_history'),
]
