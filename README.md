# Hotel Booking Website (Villagio)

**Final Assignment**

Villagio is a comprehensive hotel booking system developed using Django REST Framework, featuring user authentication, hotel and booking management, payment processing, and review functionalities. This application supports CRUD operations for hotels and bookings, secure payments via SSLCommerz, and integrates.

- **Frontend Live Site:** [Villagio](https://hotel-front-website.netlify.app/)
- **Backend Live Site:** [Render](https://hotel-backend-arcx.onrender.com/)
- **Frontend GitHub:** [Hotel-Booking-Frontend](https://github.com/mohammadarmanhossen/hotel_front)
- **Backend GitHub:** [Hotel-Booking-Website-Backend](https://github.com/mohammadarmanhossen/hotel_backend)

### User Access Information
- **Admin Role:**
```
Username: arman
Password:123
```

- **Normal User:**
```
Username: arman404
Password: Arman404@
```
---

## Key Features
- **User Authentication** via Gmail OAuth
- **CRUD Operations** for hotel and booking management
- **SSLCommerz Payment Integration** for secure payments
- **Hotel Review System** for customer feedback
- **Scalable PostgreSQL Database** with Django Rest Framework API

---

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** OAuth2 via Gmail
- **Payment Gateway:** SSLCommerz
- **Frontend (Optional):** React/Vue (deployed on Netlify)

---

## Installation and Setup

1. **Clone the repository:**
 ```bash
 
git clone https://github.com/mohammadarmanhossen/hotel_backend
cd hotel_backend
```

Install dependencies:
```
pip install -r requirements.txt

```
Run migrations:
```
 python manage.py migrate
```

Create a superuser:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```

Run Tests:

```
python manage.py runserver
```
