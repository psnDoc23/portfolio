from django.db import models


class Job(models.Model):  # new class, job
    image = models.ImageField(upload_to='images/')  # inherits from fileField
    summary = models.CharField(max_length=200)

    # add so that actual name of posts show up in admin console (rather than job (1), etc.)
    def __str__(self):
        return self.summary


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    current_pos = models.CharField(max_length=200)
