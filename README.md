# thingslist
A web application that lets you post Things, and respond to other people's Things.

# Installation and build procedure

## Clone the project

`git clone https://github.com/pgalic96/thingslist.git`
## Create and start a virtual environment
```
virtualenv env
source env/bin/activate
```
## Go to project directory and install the project dependencies (Django 1.10):
`pip3 install -r requirements.txt`

## Migrate the database
```
python3 manage.py migrate

```

## Obtain a secret key
1. [Generate a key here](https://www.miniwebtool.com/django-secret-key-generator/)
2. Copy and paste the link in `settings.py` under `SECRET_KEY`

## Create admin account
`python3 manage.py createsuperuser`
## Run the server
1. Run `python3 manage.py runserver`
2. Open localhost:8000 on your browser to view the app.
