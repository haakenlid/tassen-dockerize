#!/bin/bash

function run {
  # Start process as unprivileged user
  # Use `exec` to replace original process.
  # This makes it possible for Docker to send signals to the process.
  exec su $(id -nu 1000) -c "$@"
}

case $1 in
  jupyter)
    run "django-admin shell_plus --notebook"
    ;;
  django-admin)
    /app/wait-for-it.sh postgres:5432
    shift  # discard first argument
    run "django-admin $@"
    ;;
  runserver)
    echo 'starting django runserver'
    run 'django-admin runserver_plus'
    ;;
  uwsgi)
    echo 'starting django uwsgi'
    run 'uwsgi uwsgi.ini'
    ;;
  celerybeat)
    echo 'starting celery beat'
    run 'celery beat -A universitas'
    ;;
  celery)
    echo 'starting celery workers'
    run 'celery worker -A universitas'
    ;;
  *)
    exec "$@"; exit
    ;;
esac

