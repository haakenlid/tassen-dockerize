#!/bin/bash

case $1 in
  build)
    exec npm run build
  *)
    exec "$@"
    ;;
esac

