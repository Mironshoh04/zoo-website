# WildWorld Zoo 🦁

A modern, responsive web application for managing and showcasing zoo animals built with Django. The application features a beautiful homepage, animal management system, user authentication, and an admin interface.

## Features

- 🏠 **Beautiful Homepage** - Modern landing page with hero section, features, and contact information
- 🦒 **Animal Management** - View and manage zoo animals with images and detailed information
- 👤 **User Authentication** - Login and signup functionality
- 📱 **Responsive Design** - Mobile-friendly interface with modern styling
- 🎨 **Modern UI** - Bootstrap 5, Font Awesome icons, and custom CSS animations
- 🔧 **Admin Interface** - Django admin for easy content management

## Technologies Used

- **Backend**: Django 4.x, Python 3.11+
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (default), easily configurable for PostgreSQL/MySQL
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Poppins, Playfair Display)

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation & Setup

### 1. Clone the Project

```bash
git clone https://github.com/Mironshoh04/zoo-website.git
cd zoo-website
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install dependencies
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### 5. Collect Static Files (if needed)

```bash
python manage.py collectstatic
```

## Running the Application

### Development Server

```bash
# Start the development server
python manage.py runserver

# The application will be available at:
# http://127.0.0.1:8000/
```

### Access Different Sections

- **Homepage**: http://127.0.0.1:8000/
- **Animals**: http://127.0.0.1:8000/animals/
- **Login**: http://127.0.0.1:8000/accounts/login/
- **Sign Up**: http://127.0.0.1:8000/accounts/signup/
- **Admin**: http://127.0.0.1:8000/admin/ (requires superuser)

## Project Structure

```
ZooDefault/
├── wildworldzoo/           # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── templates/         # Base templates
│   │   └── base.html      # Main template with styling
│   └── static/            # Static files (CSS, JS, images)
├── home/                  # Home app
│   ├── views.py           # Homepage and about views
│   ├── urls.py            # Home app URLs
│   └── templates/home/    # Home templates
├── animals/               # Animals app
│   ├── models.py          # Animal model
│   ├── views.py           # Animal views
│   ├── urls.py            # Animals app URLs
│   └── templates/animals/ # Animal templates
├── accounts/              # User authentication app
│   ├── views.py           # Auth views
│   ├── forms.py           # Auth forms
│   ├── urls.py            # Auth URLs
│   └── templates/accounts/ # Auth templates
├── media/                 # User uploaded files
│   └── animal_images/     # Animal images
├── manage.py              # Django management script
└── db.sqlite3            # SQLite database
```

## Key Features Explained

### Homepage
- **Hero Section**: Eye-catching banner with call-to-action buttons
- **Features Section**: Showcases zoo capabilities with animated cards
- **About Section**: Information about the zoo with statistics
- **Animals Preview**: Overview of animal categories
- **Contact Section**: Contact information and details

### Animal Management
- View all animals in a grid layout
- Animal details with images and information
- Admin interface for adding/editing animals

### User Authentication
- User registration and login
- Session management
- Protected routes

## Configuration

### Database Configuration
The project uses SQLite by default. To use PostgreSQL or MySQL, update `DATABASES` in `wildworldzoo/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Media Files
Animal images are stored in `media/animal_images/`. Make sure the `media/` directory has proper write permissions.

### Static Files
CSS, JavaScript, and other static files are served from the `static/` directory during development.

## Adding Content

### Adding Animals (via Admin)
1. Create a superuser: `python manage.py createsuperuser`
2. Go to http://127.0.0.1:8000/admin/
3. Login with superuser credentials
4. Navigate to "Animals" section
5. Add new animals with images and details

### Customizing Styling
- Main styles are in `wildworldzoo/templates/base.html`
- CSS variables for easy theme customization
- Responsive design with Bootstrap 5

## Troubleshooting

### Common Issues

1. **"No such table" error**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

3. **Permission denied on media files**
   - Check file permissions on `media/` directory
   - Ensure Django has write access

4. **Virtual environment issues**
   - Make sure the virtual environment is activated
   - Reinstall dependencies if needed

### Development Tips

- Use `python manage.py runserver 0.0.0.0:8000` to access from other devices on the network
- Enable Django debug mode in development: `DEBUG = True` in settings.py
- Check Django logs in the terminal for error details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Feel free to use and modify as needed.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review Django documentation: https://docs.djangoproject.com/
3. Check terminal output for error messages

---

**Enjoy exploring the WildWorld Zoo! 🎉**