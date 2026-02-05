# Student System API

A Django REST Framework API for student registration, authentication, and job listings.

## Setup

```bash
cd student_system
python -m venv .venv
.venv\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### 1. Register Student
```
POST /api/students/register/
```
```json
{
  "full_name": "John Doe",
  "email": "john@gmail.com",
  "mobile": "9999999999",
  "password": "123456"
}
```

### 2. Login
```
POST /api/students/login/
```
```json
{
  "email": "john@gmail.com",
  "password": "123456"
}
```
Returns JWT access and refresh tokens.

### 3. View Jobs (Authenticated)
```
GET /api/jobs/
Authorization: Bearer <access_token>
```
Returns list of available jobs. Requires valid JWT token.

### 4. Admin Job Management
```
GET/POST/PUT/DELETE /api/admin/jobs/
Authorization: Bearer <admin_token>
```
Admin-only endpoints for managing job listings.

## Authentication

Uses JWT (JSON Web Tokens). Include the access token in request headers:
```
Authorization: Bearer <your_access_token>
```

## Tech Stack

- Django 6.0
- Django REST Framework
- SimpleJWT for authentication
- SQLite database
