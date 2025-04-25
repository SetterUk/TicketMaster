import os
import django
from datetime import datetime, time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_booking_system.settings')
django.setup()

from booking.models import Show

# Clear existing shows
Show.objects.all().delete()

# Add new shows
shows_data = [
    # Concerts
    {
        'title': 'Coldplay: Music of the Spheres World Tour',
        'description': 'Join Coldplay for an unforgettable night of music and lights.',
        'date': '2024-06-20',
        'time': '20:00',
        'location': 'Wembley Stadium',
        'price': 129.99,
        'total_seats': 200,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3'
    },
    {
        'title': 'Taylor Swift: The Eras Tour',
        'description': 'A journey through all of Taylor Swift\'s musical eras.',
        'date': '2024-06-25',
        'time': '19:00',
        'location': 'Twickenham Stadium',
        'price': 159.99,
        'total_seats': 300,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3'
    },
    {
        'title': 'Drake: It\'s All A Blur Tour',
        'description': 'Join Drake for an unforgettable night of hip-hop and R&B.',
        'date': '2024-08-20',
        'time': '20:00',
        'location': 'The O2 Arena',
        'price': 139.99,
        'total_seats': 250,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3'
    },
    # Theater
    {
        'title': 'The Phantom of the Opera',
        'description': 'Experience the magic of Andrew Lloyd Webber\'s masterpiece in this spectacular production.',
        'date': '2024-05-15',
        'time': '19:30',
        'location': 'Royal Opera House',
        'price': 89.99,
        'total_seats': 150,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d'
    },
    {
        'title': 'Hamilton',
        'description': 'The revolutionary story of America\'s founding father Alexander Hamilton.',
        'date': '2024-07-10',
        'time': '19:00',
        'location': 'Victoria Palace Theatre',
        'price': 99.99,
        'total_seats': 120,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d'
    },
    {
        'title': 'Wicked',
        'description': 'The untold story of the witches of Oz.',
        'date': '2024-05-20',
        'time': '19:30',
        'location': 'Apollo Victoria Theatre',
        'price': 85.99,
        'total_seats': 180,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d'
    },
    # Sports
    {
        'title': 'Premier League: Arsenal vs Manchester United',
        'description': 'Witness one of the biggest rivalries in English football.',
        'date': '2024-09-15',
        'time': '15:00',
        'location': 'Emirates Stadium',
        'price': 149.99,
        'total_seats': 500,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2'
    },
    {
        'title': 'Wimbledon Championships 2024',
        'description': 'Experience the world\'s most prestigious tennis tournament.',
        'date': '2024-07-01',
        'time': '11:00',
        'location': 'All England Lawn Tennis Club',
        'price': 199.99,
        'total_seats': 300,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2'
    },
    {
        'title': 'Six Nations Rugby: England vs France',
        'description': 'Watch the intense rivalry between England and France in the Six Nations Championship.',
        'date': '2024-03-16',
        'time': '16:45',
        'location': 'Twickenham Stadium',
        'price': 129.99,
        'total_seats': 400,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2'
    },
    # Comedy
    {
        'title': 'Trevor Noah: Off The Record Tour',
        'description': 'The Daily Show host brings his unique perspective on world events.',
        'date': '2024-10-05',
        'time': '20:00',
        'location': 'The O2 Arena',
        'price': 79.99,
        'total_seats': 200,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17'
    },
    {
        'title': 'Ricky Gervais: Armageddon Tour',
        'description': 'The award-winning comedian returns with his new show.',
        'date': '2024-11-15',
        'time': '19:30',
        'location': 'The SSE Arena',
        'price': 89.99,
        'total_seats': 180,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17'
    },
    {
        'title': 'Kevin Hart: Reality Check Tour',
        'description': 'The global comedy superstar brings his hilarious new show.',
        'date': '2024-12-10',
        'time': '20:00',
        'location': 'The O2 Arena',
        'price': 99.99,
        'total_seats': 250,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17'
    }
]

for show_data in shows_data:
    # Convert date string to datetime.date object
    date = datetime.strptime(show_data['date'], '%Y-%m-%d').date()
    # Convert time string to datetime.time object
    time_obj = datetime.strptime(show_data['time'], '%H:%M').time()
    
    Show.objects.create(
        title=show_data['title'],
        description=show_data['description'],
        date=date,
        time=time_obj,
        location=show_data['location'],
        price=show_data['price'],
        total_seats=show_data['total_seats'],
        image_url=show_data['image_url']
    )

print("Successfully added all shows!") 