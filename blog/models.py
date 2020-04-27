from django.db import models


class Blog(models.Model):  # new class, blog
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/')  # ImageField inherits from FileField
    body = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
