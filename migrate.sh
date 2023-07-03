#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"maxmandar@gmail.com"}

cd /app/

/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput