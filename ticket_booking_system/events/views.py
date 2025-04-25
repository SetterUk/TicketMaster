# Sample events data (in a real application, this would come from a database)
sample_events = [
    # Concerts
    {
        'id': 1,
        'title': 'Coldplay: Music of the Spheres World Tour',
        'description': 'Join Coldplay for an unforgettable night of music and lights.',
        'date': '2024-06-20',
        'time': '20:00',
        'venue': 'Wembley Stadium',
        'category': 'Concerts',
        'price': 129.99,
        'available_seats': 200,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29uY2VydHxlbnwwfHwwfHx8MA%3D%3D'
    },
    {
        'id': 2,
        'title': 'Taylor Swift: The Eras Tour',
        'description': 'A journey through all of Taylor Swift\'s musical eras.',
        'date': '2024-06-25',
        'time': '19:00',
        'venue': 'Twickenham Stadium',
        'category': 'Concerts',
        'price': 159.99,
        'available_seats': 300,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29uY2VydHxlbnwwfHwwfHx8MA%3D%3D'
    },
    {
        'id': 3,
        'title': 'Drake: It\'s All A Blur Tour',
        'description': 'Join Drake for an unforgettable night of hip-hop and R&B.',
        'date': '2024-08-20',
        'time': '20:00',
        'venue': 'The O2 Arena',
        'category': 'Concerts',
        'price': 139.99,
        'available_seats': 250,
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29uY2VydHxlbnwwfHwwfHx8MA%3D%3D'
    },
    # Theater
    {
        'id': 4,
        'title': 'The Phantom of the Opera',
        'description': 'Experience the magic of Andrew Lloyd Webber\'s masterpiece in this spectacular production.',
        'date': '2024-05-15',
        'time': '19:30',
        'venue': 'Royal Opera House',
        'category': 'Theater',
        'price': 89.99,
        'available_seats': 150,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3BlcmF8ZW58MHx8MHx8fDA%3D'
    },
    {
        'id': 5,
        'title': 'Hamilton',
        'description': 'The revolutionary story of America\'s founding father Alexander Hamilton.',
        'date': '2024-07-10',
        'time': '19:00',
        'venue': 'Victoria Palace Theatre',
        'category': 'Theater',
        'price': 99.99,
        'available_seats': 120,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3BlcmF8ZW58MHx8MHx8fDA%3D'
    },
    {
        'id': 6,
        'title': 'Wicked',
        'description': 'The untold story of the witches of Oz.',
        'date': '2024-05-20',
        'time': '19:30',
        'venue': 'Apollo Victoria Theatre',
        'category': 'Theater',
        'price': 85.99,
        'available_seats': 180,
        'image_url': 'https://images.unsplash.com/photo-1514306199707-1b1b4feb4b4d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3BlcmF8ZW58MHx8MHx8fDA%3D'
    },
    # Sports
    {
        'id': 7,
        'title': 'Premier League: Arsenal vs Manchester United',
        'description': 'Witness one of the biggest rivalries in English football.',
        'date': '2024-09-15',
        'time': '15:00',
        'venue': 'Emirates Stadium',
        'category': 'Sports',
        'price': 149.99,
        'available_seats': 500,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BvcnR8ZW58MHx8MHx8fDA%3D'
    },
    {
        'id': 8,
        'title': 'Wimbledon Championships 2024',
        'description': 'Experience the world\'s most prestigious tennis tournament.',
        'date': '2024-07-01',
        'time': '11:00',
        'venue': 'All England Lawn Tennis Club',
        'category': 'Sports',
        'price': 199.99,
        'available_seats': 300,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BvcnR8ZW58MHx8MHx8fDA%3D'
    },
    {
        'id': 9,
        'title': 'Six Nations Rugby: England vs France',
        'description': 'Watch the intense rivalry between England and France in the Six Nations Championship.',
        'date': '2024-03-16',
        'time': '16:45',
        'venue': 'Twickenham Stadium',
        'category': 'Sports',
        'price': 129.99,
        'available_seats': 400,
        'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BvcnR8ZW58MHx8MHx8fDA%3D'
    },
    # Comedy
    {
        'id': 10,
        'title': 'Trevor Noah: Off The Record Tour',
        'description': 'The Daily Show host brings his unique perspective on world events.',
        'date': '2024-10-05',
        'time': '20:00',
        'venue': 'The O2 Arena',
        'category': 'Comedy',
        'price': 79.99,
        'available_seats': 200,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29tZWR5fGVufDB8fDB8fHww'
    },
    {
        'id': 11,
        'title': 'Ricky Gervais: Armageddon Tour',
        'description': 'The award-winning comedian returns with his new show.',
        'date': '2024-11-15',
        'time': '19:30',
        'venue': 'The SSE Arena',
        'category': 'Comedy',
        'price': 89.99,
        'available_seats': 180,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29tZWR5fGVufDB8fDB8fHww'
    },
    {
        'id': 12,
        'title': 'Kevin Hart: Reality Check Tour',
        'description': 'The global comedy superstar brings his hilarious new show.',
        'date': '2024-12-10',
        'time': '20:00',
        'venue': 'The O2 Arena',
        'category': 'Comedy',
        'price': 99.99,
        'available_seats': 250,
        'image_url': 'https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29tZWR5fGVufDB8fDB8fHww'
    }
]

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

def event_list(request):
    category = request.GET.get('category')
    if category:
        events = [event for event in sample_events if event['category'].lower() == category.lower()]
    else:
        events = sample_events
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    try:
        event = next(event for event in sample_events if event['id'] == event_id)
    except StopIteration:
        raise Http404("Event not found")
    return render(request, 'events/event_detail.html', {'event': event})

def book_ticket(request, event_id):
    if request.method == 'POST':
        try:
            event = next(event for event in sample_events if event['id'] == event_id)
            quantity = int(request.POST.get('quantity', 0))
            
            if quantity <= 0:
                messages.error(request, 'Please enter a valid number of tickets.')
            elif quantity > event['available_seats']:
                messages.error(request, 'Not enough seats available.')
            else:
                # In a real application, you would save the booking to a database here
                messages.success(request, f'Successfully booked {quantity} ticket(s) for {event["title"]}!')
                return redirect('events:event_detail', event_id=event_id)
        except StopIteration:
            raise Http404("Event not found")
    
    return redirect('events:event_detail', event_id=event_id) 