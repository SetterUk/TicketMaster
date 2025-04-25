from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep Django admin for emergency access
    path('auth/', include('authentication.urls')),
    path('admin-panel/', include('adminpanel.urls')),
    path('', include('booking.urls')),
]
