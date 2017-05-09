from django.db import models

class House(models.Model):
    name = models.CharField(null=True, max_length=40)
    motto = models.CharField(null=True, max_length=50, blank=True)
    sigil = models.FileField()
    region = models.CharField(max_length=40)
    major = models.BooleanField()

    @property
    def image_url(self):
        return self.sigil.url

    def __str__(self):
        return self.name
