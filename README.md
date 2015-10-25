Raspberrywhite
==============
[![Build Status][travis-image]][travis-url] [![Coveralls Status][coveralls-image]][coveralls-url]

Your tiny social player. Use your MP3 collection to create a modern, portable and funny jukebox with Raspberry Pi.

Install dependencies
--------------------

    $ pip install -r requirements.txt

Make it running
---------------

    $ ./run.sh

Hacking ideas
-------------
Coming soon...

Test
----
Enter your virtual env and install requirements

    $ pip install -r requirements-test.txt

Launch

    $ python manage.py test

Environment Variables
---------------------

These environment variables must be set before running the application.

  * RASPBERRYWHITE_SECRET_KEY: random string that is used to set Django SECRET_KEY
  * RASPBERRYWHITE_DEBUG: Django DEBUG setting
  * RASPBERRYWHITE_TEMPLATE_DEBUG: Django TEMPLATE_DEBUG setting
  * RASPBERRYWHITE_ALLOWED_HOSTS: Django ALLOWED_HOSTS setting
  * RASPBERRYWHITE_REDIS_HOST: Redis hostname
  * RASPBERRYWHITE_REDIS_PORT: Redis port
  * RASPBERRYWHITE_REDIS_DB: Redis database name
  * RASPBERRYWHITE_LOGIN_REDIRECT_URL: url where redirect to after the authentication
  * RASPBERRYWHITE_SOCIAL_AUTH_FACEBOOK_KEY: KEY for Facebook api
  * RASPBERRYWHITE_SOCIAL_AUTH_FACEBOOK_SECRET: secret for Facebook api
  * RASPBERRYWHITE_STATIC_URL: Django STATIC_URL

[travis-url]: https://travis-ci.org/raspberrywhite/raspberrywhite
[travis-image]: http://img.shields.io/travis/raspberrywhite/raspberrywhite.svg

[coveralls-url]: https://coveralls.io/r/raspberrywhite/raspberrywhite
[coveralls-image]: http://img.shields.io/coveralls/raspberrywhite/raspberrywhite/master.svg
