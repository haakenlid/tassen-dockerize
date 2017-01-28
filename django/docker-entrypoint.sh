#!/bin/bash

RUNAS=lancelot  # user to exec as
POSTGRES='db:5432'
ARG=${1:-runserver}
shift  # discard first argument

function run {
  # Start process as unprivileged user
  # Use `exec` to replace original process.
  # This makes it possible for Docker to send signals to the process.
  exec su -m $RUNAS -c "$@"
}

case $ARG in
  bash)
    exec /bin/bash
    ;;
  django-admin)
    /app/wait-for-it.sh $POSTGRES
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
    echo "unknown argument \"$ARG\". Try django-admin | runserver | migrate | celery | bash"
    exit 1
    ;;
esac

