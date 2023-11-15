#!/bin/bash

python3 ./PokeServiceMain/manage.py migrate
python3 ./PokeServiceMain/manage.py runserver 0.0.0.0:8000
