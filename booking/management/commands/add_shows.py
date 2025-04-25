from django.core.management.base import BaseCommand
from booking.models import Show, Category
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Adds sample shows to the database'

    def handle(self, *args, **options):
        # Create categories if they don't exist
        categories = ['Concerts', 'Theater', 'Sports', 'Comedy', 'Movies']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        # Sample shows data
        shows_data = [
            {
                'title': 'The Beatles Tribute Concert',
                'description': 'Experience the magic of The Beatles with this amazing tribute band.',
                'date': datetime.now() + timedelta(days=7),
                'time': '19:00',
                'location': 'Grand Concert Hall',
                'price': 50.00,
                'total_seats': 1000,
                'available_seats': 1000,
                'category': 'Concerts'
            },
            {
                'title': 'Romeo and Juliet',
                'description': 'Classic Shakespeare play performed by the National Theater Company.',
                'date': datetime.now() + timedelta(days=14),
                'time': '20:00',
                'location': 'Royal Theater',
                'price': 40.00,
                'total_seats': 500,
                'available_seats': 500,
                'category': 'Theater'
            },
            {
                'title': 'Premier League Match',
                'description': 'Exciting football match between top teams.',
                'date': datetime.now() + timedelta(days=10),
                'time': '15:00',
                'location': 'City Stadium',
                'price': 60.00,
                'total_seats': 50000,
                'available_seats': 50000,
                'category': 'Sports'
            },
            {
                'title': 'Stand-up Comedy Night',
                'description': 'An evening of laughter with top comedians.',
                'date': datetime.now() + timedelta(days=5),
                'time': '21:00',
                'location': 'Comedy Club',
                'price': 30.00,
                'total_seats': 200,
                'available_seats': 200,
                'category': 'Comedy'
            },
            {
                'title': 'Movie Premiere: Action Hero',
                'description': 'World premiere of the latest blockbuster action movie.',
                'date': datetime.now() + timedelta(days=3),
                'time': '18:00',
                'location': 'Cinema City',
                'price': 25.00,
                'total_seats': 300,
                'available_seats': 300,
                'category': 'Movies'
            }
        ]

        # Add shows to database
        for show_data in shows_data:
            category = Category.objects.get(name=show_data['category'])
            Show.objects.get_or_create(
                title=show_data['title'],
                defaults={
                    'description': show_data['description'],
                    'date': show_data['date'],
                    'time': show_data['time'],
                    'location': show_data['location'],
                    'price': show_data['price'],
                    'total_seats': show_data['total_seats'],
                    'available_seats': show_data['available_seats'],
                    'category': category
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample shows!')) 