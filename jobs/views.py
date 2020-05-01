from django.shortcuts import render
from .models import Job, Person


def home(request):
    jobs = Job.objects  # django magically grabs all jobs from database
    persons = Person.objects  # same for persons
    return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'persons': persons
    })
