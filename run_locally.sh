#!/bin/bash
activate="`pwd`/env/bin/activate"
. "$activate"
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver --settings=django_fbot.dev_settings
