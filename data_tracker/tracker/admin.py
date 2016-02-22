from django.contrib import admin
from .models import Tracker, TrackerUser, TrackerGroup
#TODO from .models import SubTracker

# Register your models here.

admin.site.register(Tracker)
#admin.site.register(SubTracker)
admin.site.register(TrackerUser)
admin.site.register(TrackerGroup)

class TrackerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'pub_date', 'trackerID')
