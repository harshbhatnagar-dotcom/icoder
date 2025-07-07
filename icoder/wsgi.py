"""
WSGI config for icoder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import subprocess
import django
from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icoder.settings')  # Replace with your actual settings module

# Initialize Django before calling management commands
django.setup()

# Auto-run `collectstatic` only if staticfiles dir is empty (safe for Render Free Tier)
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
if not os.path.exists(static_dir) or not os.listdir(static_dir):
    subprocess.call(['python', 'manage.py', 'collectstatic', '--noinput'])

# Auto-run `migrate` on every start
try:
    subprocess.call(['python', 'manage.py', 'migrate'])
except Exception as e:
    print("Migration failed:", e)

# Get the actual WSGI application
application = get_wsgi_application()

