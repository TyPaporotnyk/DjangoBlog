# Django blog
This is my pet project to practice in Django/Postgres/Docker etc.
Also, I tried to make simple frontend.
In the future, I want to make this project as a complete web app and host it on the server. 
## Requirements
* Python 3.11
* Docker 24.0

## Set up web app
Create python virtual environment and load packages
```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Starting database
Start database and adminer in docker container <br>
Before start container tou should create .env file from .env.dit template and fill up it correct values
```bash
docker-compose build
docker-compose up -d
```

## Migrations
Creating migrations and applied it to database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Starting web app
```bash
python manage.py runserver
```
