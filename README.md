Raspberrywhite
==============
[![Build Status][travis-image]][travis-url] [![Coveralls Status][coveralls-image]][coveralls-url]

Your tiny social player. Use your MP3 collection to create a modern, portable and funny jukebox with Raspberry Pi.

Install dependencies
--------------------

    $ pip install -r requirements.txt
    
Troubleshouting
---------------

Under OSX 10.10.5 and 10.11.x is it possible to get an error while installing ```gevent`` package from **pip** it can be fixed installing gevent with this command:

```
CFLAGS='-std=c99' pip install gevent==1.0.1
```

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

[travis-url]: https://travis-ci.org/raspberrywhite/raspberrywhite
[travis-image]: http://img.shields.io/travis/raspberrywhite/raspberrywhite.svg

[coveralls-url]: https://coveralls.io/r/raspberrywhite/raspberrywhite
[coveralls-image]: http://img.shields.io/coveralls/raspberrywhite/raspberrywhite/master.svg
