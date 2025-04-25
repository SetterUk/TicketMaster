from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('shows/', views.ShowListView.as_view(), name='show_list'),
    path('shows/add/', views.ShowCreateView.as_view(), name='show_add'),
    path('shows/edit/<int:show_id>/', views.ShowUpdateView.as_view(), name='show_edit'),
    path('shows/delete/<int:show_id>/', views.ShowDeleteView.as_view(), name='show_delete'),
    path('bookings/', views.BookingListView.as_view(), name='booking_list'),
]
