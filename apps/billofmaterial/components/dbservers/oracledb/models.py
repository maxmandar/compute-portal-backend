from django.db import models

# Create your models here.
class OracleDB(models.Model):
    environment = models.CharField(max_length=255)
    datacenter = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.environment} - {self.datacenter}"