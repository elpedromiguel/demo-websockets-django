# demo

steps
$ docker-compose build
$ docker-compose run --rm django python manage.py migrate
$ docker-compose run --rm django python manage.py createsuperuser
$ docker-compose up