#!/bin/bash -x

export PYTHONUNBUFFERED=1
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR=$(dirname "$BASE_DIR")

wait-for-it $DATABASE_HOST:$DATABASE_PORT

if [ "$CI" == "true" ]; then
    pip3 install coverage pytest-xdist

    set -e
    # Wait until database is ready
    wait-for-it ${DATABASE_HOST:-db}:${DATABASE_PORT-5432}

    # To show migration logs
    ./manage.py test --keepdb -v 2 gaatha.tests
    pytest -ra --reuse-db -v --durations=10

    set +e
else
    py.test
fi
