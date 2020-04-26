from django.db import models


class Job(models.Model):  # new class, job
    image = models.ImageField(upload_to='images/')  # inherits from fileField
    summary = models.CharField(max_length=200)
