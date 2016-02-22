from django.contrib import admin
from .models import Tracker

# Register your models here.

admin.site.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'pub_date', 'trackerID')
