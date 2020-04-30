from django.db import models


class Blog(models.Model):  # new class, blog
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/')  # ImageField inherits from FileField
    body = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()

    # add so that actual name of posts show up in admin console (rather than blog post (1), etc.)
    def __str__(self):
        return self.title

    # Nick: "class that has a function needs to have self as a parameter" why, exactly?
    def summary(self):
        return self.body[:100]  # take first 100 chars

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')  # don't need exact DT
