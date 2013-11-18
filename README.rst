===============================
leasy
===============================

Flask app to ease interaction/transaction between leasor and leasee.


Quickstart
----------

::

    git clone https://github.com/ktal90/leasy
    cd leasy
    pip install -r requirements/dev.txt
    export LEASY_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the LEASY_ENV system environment variable.

To switch to the development environment, set ::

    export LEASY_ENV="dev"

To switch to the production environment, set ::

    export LEASY_ENV="prod"