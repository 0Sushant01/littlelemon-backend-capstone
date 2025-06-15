# littlelemon-backend-capstone
Django REST API for the Little Lemon restaurant – built as a capstone project to demonstrate backend development skills including model design, authentication, API creation, testing, and deployment.

# 🍋 Little Lemon API – Capstone Project

This is the backend REST API for **Little Lemon**, a fictional restaurant. Built as part of the final capstone project in the Meta Backend Developer Certificate program, this project demonstrates core backend development skills using **Django** and the **Django REST Framework (DRF)**.

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

littlelemon/
├── littlelemon/ # Django project settings
├── restaurant/ # Main app with views, models, serializers
├── static/ # Static HTML files (if served)
├── templates/ # HTML templates
├── requirements.txt # Project dependencies
└── manage.py # Django project manager


---

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
