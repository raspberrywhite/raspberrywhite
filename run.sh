#!/bin/bash
source env.sh
redis-server &
python popmuzik.py &
gunicorn servant.wsgi --worker-class=gevent -b 0.0.0.0:8000
redis-cli shutdown
killall python
killall mpg321