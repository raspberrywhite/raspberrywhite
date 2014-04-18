Raspbarry White
===============
Your tiny social player.

Test
----
Before starting your tests you need to fill the tests/assets folder with the files extracted from this zip: https://dl.dropboxusercontent.com/u/35837126/assets.zip

Enter your virtual env and install requirements

    $ pip install -r requirements.txt

Launch

    $ nosetests tests/

To test a category run nose specifying the category directory

    $ nosetests tests/test_player

To launch a single unit test, just launch nose specifying a single python file

    $ nosetests tests/test_player/<your_test>

To create a new test just

- add a file into /tests/test_(category_you_want_to_test)
- create a file test_(something)
