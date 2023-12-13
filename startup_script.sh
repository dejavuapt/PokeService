# !/bin/bash
# python3 ./PokeServiceMain/manage.py makemigrations
# python3 ./PokeServiceMain/manage.py migrate
python3 ./PokeServiceMain/manage.py test ./PokeServiceMain/main/tests --noinput
# python3 ./PokeServiceMain/manage.py runserver 0.0.0.0:8000
