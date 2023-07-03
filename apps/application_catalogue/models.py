from django.db import models

# Create your models here.
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField()
    dr_tier = models.CharField(max_length=100)

    def __str__(self):
        return self.name