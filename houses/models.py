from django.db import models

class House(models.Model):
    name = models.CharField(null=True, max_length=40)
    motto = models.CharField(null=True, max_length=50)
    sigil = models.FileField()
    region = models.CharField()
    major = models.BooleanField()

    @property
    def image_url(self):
        return self.sigil.url
