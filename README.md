# School Management System

A simple school management system built with Django. This project allows administrators to manage students, teachers, courses, and enrollments through a basic web interface with authentication.

---

## 📚 Features

- Create, update, and delete students, teachers, courses, and enrollments
- User authentication (login and logout)
- Protected views with `login_required`
- Admin interface enabled
- Basic styling with a base HTML template
- Unit tests for models and views

---

## 🛠️ Tech Stack

- Python 3
- Django 4.x
- SQLite (default Django database)
- HTML/CSS (Django templates)
- Unit testing with Django's `TestCase`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/CharlesNeres/school-management.git
cd school-management
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧪 Running Tests

To run tests:

```bash
python manage.py test
```

---

## 📁 Project Structure

```
school_management/
├── courses/
├── school/
├── school_management/
├── templates/
├── users/
├── manage.py
└── README.md
```

---

## ✍️ Author

Developed by Charles Junior — Software Developer with experience in Django and front-end technologies.

---

## 📜 License

This project is licensed under the MIT License.
