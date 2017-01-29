#!/bin/bash

function run {
  # Start process as unprivileged user
  # Use `exec` to replace original process.
  # This makes it possible for Docker to send signals to the process.
  exec su -p $(id -nu 1000) -c "$@"
}

case $1 in
  django-admin)
    /app/wait-for-it.sh postgres:5432
    shift  # discard first argument
    run "django-admin $@"
    ;;
  runserver)
    echo 'starting django runserver'
    run 'django-admin runserver 0.0.0.0:8000'
    ;;
  uwsgi)
    echo 'starting django uwsgi'
    run 'uwsgi uwsgi.ini'
    ;;
  celery)
    echo 'starting celery workers'
    run 'celery worker -A universitas'
    ;;
  *)
    exec "$@"
    ;;
esac

