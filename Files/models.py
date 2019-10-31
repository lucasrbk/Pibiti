from django.db import models
from django.urls import reverse
# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=3)
    archive = models.FileField()

    def get_absolute_url(self):
        return reverse()

    def __str__(self):
        return self.name + " " + self.type + " " + str(self.archive)
