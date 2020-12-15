#!/bin/bash

rm -rf vacaplusapi/migrations
rm db.sqlite3
python manage.py makemigrations vacaplusapi
python manage.py migrate
python manage.py loaddata user
python manage.py loaddata tokens
python manage.py loaddata vacausers
python manage.py loaddata location
python manage.py loaddata activity
