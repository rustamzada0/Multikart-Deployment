# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multikart.settings")
app = Celery("multikart")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# celery -A django_celery worker
# celery -A multikart worker --beat --scheduler django --loglevel=info

# celery -A multikart worker -l info