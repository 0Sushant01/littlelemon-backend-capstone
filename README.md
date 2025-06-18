
# 🍋 littlelemon-backend-capstone

Django REST API for the Little Lemon restaurant – built as a capstone project to demonstrate backend development skills including model design, authentication, API creation, testing, and deployment.

<<<<<<< HEAD
=======
# 🍋 Little Lemon API – Capstone Project

This is the backend REST API for **Little Lemon**, a fictional restaurant. Built as part of the final capstone project in the Meta Backend Developer Certificate program, this project demonstrates core backend development skills using **Django** and the **Django REST Framework (DRF)**.

>>>>>>> 
---

## 🚀 Project Features

- ✅ User registration, login, and logout
- ✅ Role-based user access (Manager, Delivery Crew, Customer)
- ✅ Menu management (CRUD operations)
- ✅ Table booking functionality
- ✅ Cart and order management
- ✅ REST API secured with authentication
- ✅ Unit testing and API testing with Insomnia
- ✅ MySQL database integration

---

## 🛠️ Tech Stack

- **Backend Framework**: Django 4.x, Django REST Framework
- **Authentication**: Token-based Authentication (Djoser)
- **Database**: MySQL
- **Testing Tools**: Unittest, Insomnia
- **Version Control**: Git & GitHub

---

## 📂 Project Structure

<<<<<<< HEAD
```
=======
>>>>>>> 
littlelemon/
├── littlelemon/                # Project-level settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/                 # Main Django app (views, models, serializers, urls)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/                     # Static files (CSS, JS, images)
│   └── ...
│
├── templates/                  # HTML templates
│   └── ...
│
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
└── README.md                   # Project documentation


## 🔐 Authentication & Roles

The API supports role-based access:
- **Manager**: Full access to manage users, menu, and orders
- **Customer**: Can browse menu and place orders
- **Delivery Crew**: Can view and update assigned orders

Authentication handled using **Djoser** with token-based auth.

---

## ✅ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/little-lemon-api-capstone.git
   cd little-lemon-api-capstone
<<<<<<< HEAD
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your database (MySQL) in `settings.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

---

## 📮 API Endpoints Overview

| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| POST   | `/auth/users/`               | Register a new user              |
| POST   | `/auth/token/login/`         | Login and obtain token           |
| POST   | `/auth/token/logout/`        | Logout the current user          |
| GET    | `/menu-items/`               | View menu items                  |
| POST   | `/menu-items/`               | Add a new menu item (Manager)    |
| GET    | `/cart/menu-items/`          | View cart items (Customer)       |
| POST   | `/cart/menu-items/`          | Add item to cart (Customer)      |
| POST   | `/orders/`                   | Place an order (Customer)        |
| GET    | `/orders/`                   | View all orders (Manager)        |
| GET    | `/bookings/`                 | View or create bookings          |

> 💡 Full API documentation available via [DRF browsable interface](http://127.0.0.1:8000/) after starting the server.

---

## 🧪 Testing

- **Run unit tests:**
   ```bash
   python manage.py test
   ```

- **API Testing Tool Used**: [Insomnia](https://insomnia.rest/)  
  Import your endpoints and test with authentication headers and payloads.

---

## 🌐 Deployment (Optional)

You can deploy this project using:

- **Render**
- **Railway**
- **Heroku (with ClearDB or Planetscale)**
- **Docker** (with `docker-compose`)

---

## 📌 License

This project is for educational purposes as part of the **Meta Backend Developer Certificate** on Coursera.

---

## 🙌 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser Auth Library](https://djoser.readthedocs.io/)
- Meta & Coursera Backend Specialization

---

## 👤 Author

**Sushant**  
Capstone project submission for Coursera / Meta  

=======
>>>>>>> 
