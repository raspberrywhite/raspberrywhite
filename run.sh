#!/bin/bash
source env.sh
redis-server &
python popmuzik.py &
gunicorn servant.wsgi --worker-class=gevent -b 0.0.0.0:8000
killall redis-server
killall python