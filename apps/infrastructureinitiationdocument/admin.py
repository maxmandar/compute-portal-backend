# Register your models here.
from django.contrib import admin
from .models import IidProject

admin.site.register(IidProject)

from .models import IidRequestor

admin.site.register(IidRequestor)