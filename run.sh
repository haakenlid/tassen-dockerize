#!/bin/bash
# Build and demonize docker container
COMPOSE_FILE=docker-compose.yml:docker-compose.production.yml
docker-compose build
docker-compose run --rm webpack build 
docker-compose run --rm web django-admin migrate
docker-compose run --rm web django-admin collectstatic --noinput
docker-compose up -d
docker ps
