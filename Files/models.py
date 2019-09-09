from django.db import models


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=3)

    @property
    def __str__(self):
        return self.name + " " + self.type
