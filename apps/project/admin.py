from django.contrib import admin
from .models import *



admin.site.register(Project)
admin.site.register(ProjectAction)
admin.site.register(ProjectPermission)
admin.site.register(UserRole)

