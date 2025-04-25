# TicketMaster - Event Ticket Booking System

A Django-based web application for managing and booking event tickets.

## Features

- Event listing and detailed views
- User-friendly ticket booking interface
- Event management system
- Responsive design for all devices

## Project Structure

```
ticket_booking_system/
├── events/
│   ├── templates/
│   │   └── events/
│   │       ├── event_detail.html
│   │       └── event_list.html
│   │
│   ├── urls.py
│   └── views.py
├── templates/
│   └── base.html
└── ticket_booking_system/
    ├── settings.py
    └── urls.py
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/SetterUk/TicketMaster.git
   cd TicketMaster
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- Python

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or suggestions, please open an issue in the repository. 