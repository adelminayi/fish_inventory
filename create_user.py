# create_super.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fish_inventory.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "a.minayi@gmail.com", "admin")
    print("Superuser created")
else:
    print("Superuser already exists")
