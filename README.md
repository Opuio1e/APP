# Neon Admin Dashboard

A sleek, modern admin dashboard built with Django, featuring a vibrant neon design theme.

## Overview

Neon Admin Dashboard is a stylish admin interface that provides data visualization, user management, and payment tracking functionality. Its eye-catching design uses a neon color scheme with a dark gradient background to create a modern, tech-focused administrative interface.

## Features

- **User Authentication**: Secure login and registration system
- **Dashboard Analytics**: Visual representation of key metrics
- **Payment Tracking**: Monitor financial transactions
- **Responsive Design**: Optimized for different screen sizes
- **Real-time Updates**: Dynamic data visualization with Chart.js

## Tech Stack

- **Backend**: Django 5.1
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js
- **Authentication**: Django built-in auth system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/neon-admin-dashboard.git
   cd neon-admin-dashboard
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the dashboard at http://127.0.0.1:8000/

## Project Structure

```
Admin/
├── Admin/                  # Main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
├── adminapp/               # Dashboard application
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files
│   │   ├── css/            # Stylesheets
│   │   └── js/             # JavaScript files
│   ├── templates/          # HTML templates
│   │   ├── appadmin/       # Dashboard templates
│   │   └── registration/   # Auth templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py            # Custom forms
│   ├── models.py           # Data models
│   ├── tests.py
│   ├── urls.py             # App URL configuration
│   └── views.py            # View functions
└── manage.py               # Django command-line utility
```

## Usage

1. Log in using your credentials at `/login/`
2. Navigate the dashboard using the sidebar menu
3. View analytics on the main dashboard page
4. Access user management and payment information

## Customization

### Styling
The dashboard uses custom CSS for styling. The main styles are located in:
- `adminapp/static/css/dashboard.css` - Dashboard styling
- `adminapp/static/css/mylogin.css` - Login page styling

### Adding New Features
To add new features:
1. Create new templates in the `adminapp/templates/` directory
2. Add corresponding views in `views.py`
3. Update URL patterns in `urls.py`
4. Add any needed models to `models.py`

## Security Notes

- Remember to change the default `SECRET_KEY` in `settings.py` before deploying to production
- Set `DEBUG = False` in production
- Consider using a more robust database solution like PostgreSQL for production use

## License

[MIT License](LICENSE)

## Credits

- Dashboard design by [Your Name]
- Built with Django and Chart.js
