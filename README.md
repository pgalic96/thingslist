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
## Create admin account
`python manage.py createsuperuser`
## Run the server
`python manage.py runserver`
Open localhost:8000 on your browser to view the app.
