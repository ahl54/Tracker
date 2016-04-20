from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from .models import Tracker, TrackerUser, TrackerGroup, TrackerProject
from .forms import TrackerForm, LoginForm, TrackerUserCreationForm

# Define your model admins here
class TrackerUserAdmin(admin.ModelAdmin):

    form = TrackerUserCreationForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

# Register your models here.
admin.site.register(Tracker)
admin.site.register(TrackerGroup)
admin.site.register(TrackerProject)
admin.site.register(TrackerUser,TrackerUserAdmin)
admin.site.register(Permission)
