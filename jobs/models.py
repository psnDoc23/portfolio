from django.db import models


class job(models.Model):  # new class, job
    image = models.ImageField(upload_to='')  # inherits from fileField
    summary = models.CharField(max_length=200)
