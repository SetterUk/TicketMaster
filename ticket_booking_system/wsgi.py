"""
WSGI config for ticket_booking_system project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_booking_system.settings')

application = get_wsgi_application()
