#!/bin/bash -ex
docker-compose up -d --build
docker exec ceca_django_1 python manage.py migrate
docker exec ceca_django_1 python manage.py write_car_rows