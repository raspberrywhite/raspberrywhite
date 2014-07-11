#!/bin/bash

# All the settings are now read from env variables.
# Before running the project you need to seet them all in your environment.
# On Linux: change the values accordin to your own settings and put these lines in .bashrc or
# in the activate script of virtualenv.
# On Heroku: heroku config:add RASPBERRYWHITE_DEBUG="True"

export RASPBERRYWHITE_SECRET_KEY="q!8*f9eo!(=qlg@^xm955(q4ues&^3kt7a7dusl_vl=0u1dc3q"
export RASPBERRYWHITE_DEBUG="True"
export RASPBERRYWHITE_TEMPLATE_DEBUG="True"
export RASPBERRYWHITE_ALLOWED_HOSTS=""
export RASPBERRYWHITE_REDIS_HOST="localhost"
export RASPBERRYWHITE_REDIS_PORT="6379"
export RASPBERRYWHITE_REDIS_DB="2"
export RASPBERRYWHITE_LOGIN_REDIRECT_URL="/playlist/"
export RASPBERRYWHITE_SOCIAL_AUTH_FACEBOOK_KEY="497136996989028"
export RASPBERRYWHITE_SOCIAL_AUTH_FACEBOOK_SECRET="a93971a44f9b575bebed9b1b942b2dd1"
export RASPBERRYWHITE_STATIC_URL="/static/"
