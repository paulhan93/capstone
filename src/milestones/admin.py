from django.contrib import admin

# Register your models here.
from .models import Milestones    # relative import (same directory)

admin.site.register(Milestones)