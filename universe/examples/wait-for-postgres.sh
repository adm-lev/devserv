#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="NewEntry1" psql -h "$host" -d "universe" -U "webadmin" -c '\q';
do
  >&2 echo "Postgres is unavaliable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
