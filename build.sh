#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install --force-reinstall -U djangorestframework-simplejwt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py createsuperuser