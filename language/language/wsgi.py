"""
WSGI config for language project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from language import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "language.settings")


if settings.DEBUG==True:
    application = get_wsgi_application()
else: # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())



