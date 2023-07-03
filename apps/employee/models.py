from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.fullname
