#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
# python manage.py flush --no-input
python manage.py load_data pizza_data.json

gunicorn usersnack.wsgi:application --bind 0.0.0.0:$PORT