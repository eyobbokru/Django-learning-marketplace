# Django Online Marketplace

Welcome to the Django Online Marketplace project! This tutorial is designed to help beginners learn Django by building a simple online marketplace. Follow the steps below to set up and run the project on your local machine.

## Prerequisites

- Python 3.x installed on your machine.
- [Virtualenv](https://pypi.org/project/virtualenv/) for creating a virtual environment.

## Getting Started

1. **Clone the repository to your local machine:**
    ```bash
    git clone https://github.com/your-username/django-online-marketplace.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd django-online-marketplace
    ```

3. **Create a virtual environment:**
    ```bash
    virtualenv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

5. **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser account:**
    ```bash
    python manage.py createsuperuser
    ```

8. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

9. **Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).** You should see the Django Online Marketplace homepage.

10. **Access the admin panel by navigating to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the superuser credentials created earlier.**

## Features

- User authentication and authorization.
- Product listing and details pages.
- Admin panel for managing products and orders.

## Acknowledgments

- Thanks to FreecodeCamp for the inspiration and tutorial on building an online marketplace with Django. Check out the [YouTube Channel](https://www.youtube.com/watch?v=ZxMB6Njs3ck)https://www.youtube.com/watch?v=ZxMB6Njs3ck) for the full tutorial.
