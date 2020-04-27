from django.contrib import admin
from .models import Blog

# want the following to show up in the admin page
admin.site.register(Blog)
