# Google Authentication API

- This project provides an API for authenticating users with Google using Django and Django REST Framework.

## Features
- Authenticate users with Google ID Tokens.
- Generate JWT tokens (access and refresh) for authenticated users.
- Store user profiles in the database.
- Simple test cases for the authentication endpoint.

## Requirements
- Python 3.x
- Django
- Django REST Framework
- Django REST Framework Simple JWT



Create a virtual environment and activate it:
``` bash
python3 -m venv venv
source venv/bin/activate 
```
## Install the dependencies:

Install Django:

``` bash 
pip install Django>=3.0,<4.0
```

Install Django REST Framework:

``` bash 
pip install djangorestframework>=3.12,<4.0
```

Install Django REST Framework Simple JWT:

``` bash 
pip install djangorestframework-simplejwt>=4.7.2,<5.0 
```
### Set up Google OAuth Credentials:

Obtain OAuth 2.0 credentials from the Google Developer Console.
Set up the GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET in your environment variables.

### Apply migrations:

```bash 
python manage.py migrate 
```
### Run the development server:

```bash 
python manage.py runserver
```

## Usage

### Endpoints

GET /google-authentication/: Returns a simple "Hello World!" message.
POST /google-authentication/: Accepts an ID token from Google, verifies it, and returns JWT tokens for authenticated users.

### Request Body for POST /google-authentication/

```bash
{
    "id_token": "YOUR_GOOGLE_ID_TOKEN"
}
```

Success (200 OK):
```bash
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

Invalid Token (400 BAD REQUEST):
```bash
{
    "error": "invalid id token"
}
```

Missing Token (400 BAD REQUEST):
```bash 
{
    "error": "missing id_token"
}
```

Token Verification Error (400 BAD REQUEST):
```bash
{
    "error": "Could not verify token signature"
}
```

## Running Tests
To run the tests, use the following command:

```bash
python manage.py test
```

## Project Structure
```bash
.
├── manage.py
├── app_name/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
└── requirements.txt
```

- models.py: Defines the UserProfile model.
- serializers.py: Defines the IdTokenSerializer.
- views.py: Contains the googleAuthentication API view.
- tests.py: Contains test cases for the authentication API.models.py: Defines the UserProfile model. serializers.py: Defines the IdTokenSerializer. views.py: Contains the googleAuthentication API view. tests.py: Contains test cases for the authentication API.
