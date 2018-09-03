# thingslist
A web application that lets you post Things, and respond to other people's Things.

## Virtual Environment
To run the project, create a Python3 based virtual environment 
[Virtual Environment Docs](https://docs.python.org/3/tutorial/venv.html).
Make sure to install pip in this environment and next run `pip install -r requirements.txt` from within the environment
 to install all the required packages.

## Django Database
The default database that Django uses is SQLite3. No extra configuration is needed.

## Running Django locally
To run Django locally with a test server, make sure `DEBUG` is set to `True` in `.env` and run 
`python manage.py runserver 127.0.0.1:8000`.

## Updating Django
Whenever someone updates something in Django, you might need to run some commands before you can run Django again. 
If the `models.py` file is updated, you first want to run: 
```
python manage.py makemigrations
python manage.py migrate
```
# Build procedure
Since in this project I am using only Python and Javascript which are interpreted languages, there is no need for build
procedure.

# Installation procedure
## Required packages
