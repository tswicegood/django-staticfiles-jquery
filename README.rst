django-staticfiles-jquery
=========================
Introducing jQuery to Django!


Usage
-----
This application is meant to be used with `django-staticfiles`_.  Make sure
that staticfiles setup and configured, then install this application using
`pip`_:

::

	pip install django-staticfiles-jquery

Finally, make sure that `jquery` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

	INSTALLED_APPS += ['jquery', ]


Build
-----
To build this, you need to have the jQuery `build tool chain`_ configured.
See ``support/build.py`` for more information on how data is transferred from the submodule to the Python package.

.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/
.. _build tool chain: https://github.com/jquery/jquery#how-to-build-your-own-jquery
