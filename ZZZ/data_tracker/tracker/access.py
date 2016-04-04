from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Tracker
from django.db import models

class Share():
    def addGroup():
        new_group, created = Group.objects.get_or_create(name='new_group')
        # Code to add permission to group ???
        ct = ContentType.objects.get_for_model(TrackerGroup)
        addPermission('can_add_users', 'Can add users', new_group)

    def addPermission(codename, name, group):
        permission = Permission.objects.create(codename=codename,
                                           name=name,
                                           content_type=ct)
        group.permissions.add(permission)

    def invite_to_join(email):
        #if email is not in database
        #TODO sends an email to the user provided address linking to register page
        #else
        #automatically adds user to group
        #sends a notification to the user associated with email address of their new group status

    def ask_to_join(group):
        #sends an notification to the group admin to allow a user to be added to group
