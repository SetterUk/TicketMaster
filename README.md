# TicketMaster - Event Booking System

A modern event booking system built with Django that allows users to browse and book tickets for various events including concerts, theater shows, sports events, and comedy shows.

## Features

- User Authentication (Register/Login)
- Event Browsing by Categories
- Ticket Booking System
- Custom Admin Panel
- Booking History
- Responsive Design

## Tech Stack

- **Backend:** Python 3.11, Django 5.2
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (Development), PostgreSQL (Production)
- **DevOps:** Docker, Jenkins
- **Version Control:** Git

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- Git

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TicketMaster.git
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

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit http://127.0.0.1:8000 in your browser

## Docker Setup

1. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Visit http://localhost:8000 in your browser

## CI/CD Pipeline

The project uses Jenkins for Continuous Integration and Continuous Deployment. The pipeline includes:

1. Build Stage
   - Code checkout
   - Environment setup
   - Dependency installation

2. Test Stage
   - Unit tests
   - Integration tests
   - Code quality checks

3. Deploy Stage
   - Docker image build
   - Container deployment

## Project Structure

```
TicketMaster/
├── adminpanel/           # Custom admin interface
├── authentication/       # User authentication
├── booking/             # Main booking functionality
├── templates/           # Global templates
├── static/              # Static files
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── Jenkinsfile         # Jenkins pipeline configuration
└── requirements.txt     # Python dependencies
```

## Screenshots

![Homepage](screenshots/homepage.png)
![Event Details](screenshots/event_details.png)
![Booking Page](screenshots/booking_page.png)
![Admin Dashboard](screenshots/admin_dashboard.png)

## Development

1. Create a new branch for each feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit with meaningful messages:
   ```bash
   git add .
   git commit -m "Add: Detailed description of your changes"
   ```

3. Push your changes and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

