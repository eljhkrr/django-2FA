Django Two-Factor Authentication
--------

An implementation of two-factor authentication with django.

### Features
This app supports verification via:
* QR code
* Automated voice call (via Twilio gateway)
* SMS (via Twilio gateway)

### Installation
The most recommended way to run this project is within a virtual enviroment to isolate dependency installation and leave system packages untouched.

#### steps
Install virtualenv
```
$ [sudo] pip install virtualenv
```

Create your virtual environment
```
$ virtualenv [path]
```

Activate your virtual environment
```
$ cd [path]
$ source bin/activate
```

Get the code
```
$ git clone https://github.com/TheRakken/django-2FA.git
```

Install dependencies
```
$ pip install -r requirements.txt
```

Make migrations for installed apps
```
$ manage.py makemigrations
```

Migrate models
```
$ manage.py migrate
```

Start dev server
```
$ manage.py runserver
```
