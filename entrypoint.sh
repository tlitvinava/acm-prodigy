#!/bin/bash

python3 manage.py collectstatic --noinput --no-input --clear

python3 manage.py makemigrations main

python3 manage.py migrate

exec "$@"