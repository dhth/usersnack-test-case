#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1.0
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
# python manage.py flush --no-input
python manage.py load_data pizza_data.json

exec "$@"