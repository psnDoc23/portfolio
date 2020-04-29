from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects  # django magically grabs all jobs from database
    return render(request, 'jobs/home.html', {'jobs': jobs})
