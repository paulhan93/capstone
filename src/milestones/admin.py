from django.contrib import admin
from .models import Milestones      # relative import (same directory)

# Register your models here.
admin.site.register(Milestones)