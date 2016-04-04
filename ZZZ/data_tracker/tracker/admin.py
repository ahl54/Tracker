from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tracker, TrackerUser, TrackerGroup
from .forms import TrackerForm, LoginForm, TrackerUserCreationForm

# Define your model admins here
class TrackerUserAdmin(admin.ModelAdmin):

    form = TrackerUserCreationForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

# Register your models here.
admin.site.register(Tracker)
admin.site.register(TrackerUser,TrackerUserAdmin)
admin.site.register(TrackerGroup)
