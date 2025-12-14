
# Django Accounts Project with Docker

A sample Django project featuring a **custom user authentication system** using email instead of a username, fully containerized with Docker and PostgreSQL.

---

##  Features

- Custom `User` model with email as the username
- User registration, login, and logout
- Admin panel integration for user management
- Fully Dockerized setup with PostgreSQL
- Organized templates and static files for easy customization

---

##  Prerequisites

- Docker >= 24  
- Docker Compose >= 2  
- Python 3.12+ (for local development)  
- Git  

---

##  Project Structure

my_site/
├── accounts/ # User management app
│ ├── migrations/
│ ├── templates/accounts/
│ │ ├── login.html
│ │ └── register.html
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── website/ # App for public pages (e.g., home)
├── templates/
│ └── home.html
├── my_site/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

##  Configuration

- **Custom User Model** defined in `accounts/models.py`  
- `settings.py` includes:
```python
AUTH_USER_MODEL = "accounts.User"
•	PostgreSQL database is set up with:
o	Name: testdb
o	User: bahram
o	Password: bahram
o	Host: db (Docker service)

 Running the Project with Docker
1.	Clone the repository:
git clone <repository_url>
cd django_docker_001
2.	Build and start containers:
docker-compose up -d --build
3.	Apply migrations:
docker-compose exec web python manage.py migrate
4.	Create a superuser:
docker-compose exec web python manage.py createsuperuser
5.	Access the project:
•	Website: http://localhost:8000/
•	Admin panel: http://localhost:8000/admin/

 URL Routes
Path	Description
/accounts/register/	User registration
/accounts/login/	User login
/accounts/logout/	User logout
/	Home page
/admin/	Admin panel
________________________________________
 Security Notes
•	DEBUG=True is only for development
•	ALLOWED_HOSTS=['*'] is not safe for production
•	Use environment variables for SECRET_KEY and database credentials in production

 Development Notes
•	Templates are located in templates/ and accounts/templates/accounts/
•	Forms are defined in accounts/forms.py
•	Authentication logic is in accounts/views.py and admin.py
•	You can extend the authentication system to support login via email or username by implementing a custom authentication backend

 References
•	Django Documentation
•	Docker Documentation
•	PostgreSQL Documentation

---

