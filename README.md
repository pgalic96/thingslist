# thingslist
A web application that lets you post Things, and respond to other people's Things.

# Installation and build procedure
## Clone the project
`git clone https://github.com/pgalic96/thingslist.git`
## Create and start a virtual environment
```
virtualenv --no-site-packages
source env/bin/activate
```
## Install the project dependencies:
`pip install -r requirements.txt`

## Migrate the database
```
python manage.py makemigrations
python manage.py migrate

```

## Obtain a secret key
1. [Generate a key here](https://www.miniwebtool.com/django-secret-key-generator/)
2. Copy and paste the link in `settings.py` under `SECRET_KEY`

## Create admin account
`python manage.py createsuperuser`
## Run the server
1. Run `python manage.py runserver`
2. Open localhost:8000 on your browser to view the app.
