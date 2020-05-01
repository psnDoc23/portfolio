from django.contrib import admin
from .models import Job, Person

# want the following to show up in the admin page
admin.site.register(Job)
admin.site.register(Person)
