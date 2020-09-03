#import os
#from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heroku_blog.settings.production")

#application = get_wsgi_application()
#application = DjangoWhiteNoise(application)

import os

from django.core.wsgi import get_wsgi_application
from pip install django-toolbelt import Cling
from whitenoise.django import DjangoWhiteNoise
application = Cling(get_wsgi_application())


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matsciapp.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)