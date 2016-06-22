from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Tracker, TrackerProject
from django.db import models
import requests, json

# replace dev_token with your own
dev_token = '3f540ae0a2b04211b77df7167c7b3d83'
base_url  = 'https://api.sbgenomics.com/v2'

def api(path, method='GET', data=None):
	data = json.dumps(data) if isinstance(data, dict) else None
	headers = {
		'X-SBG-Auth-Token': dev_token,
		'Accept'          : 'application/json',
		'Content-type'    : 'application/json'
	}
	response = requests.request(method, base_url + path, data=data, headers=headers)
	response_json = json.loads(response.content) if response.content else {}
	if response.status_code / 100 != 2:
		raise Exception('Server responded with status code %s.' % response.status_code)
	return response_json

def push_whitelist(project_list):
    for each_project in project_list['items']:
        member_path = '/projects/' + each_project['id'] + '/members'
        member_list = api(path = member_path)
        for each_member in member_list['items']:
            username = each_member['username']
            projects = each_project['id']
            permissions = str(each_member['permissions'])

            project = projects.split('/', 1)[1]


        try:
            p = TrackerProject.objects.get(name=projects)
        except p.DoesNotExist:
            print('Queried project does not exist...creating TrackerProject')
            #p = TrackerProject.objects.create(name=projects)

class Access():

    def addProjects(self):
        project_list = api(path = '/projects')
        push_whitelist(project_list)
            # if does not exist add TrackerProject

    def updateGroup():
        new_group, created = Group.objects.get_or_create(name='new_group')
        # Code to add permission to group ???
        ct = ContentType.objects.get_for_model(TrackerGroup)
        addPermission('can_add_users', 'Can add users', new_group)

    def updatePermissions(self):#codename, name, group):
        #permission = Permission.objects.create(codename=codename,
        #                                   name=name,
        #                                   content_type=ct)
        #group.permissions.add(permission)
        permission = Permission.objects.all()
        print(permission)
        #permission = Permission.objects.get(name='can_copy')
        #u.user_permissions.add(permission)


    #def invite_to_join(email):
        #if email is not in database
        #TODO sends an email to the user provided address linking to register page
        #else
        #automatically adds user to group
        #sends a notification to the user associated with email address of their new group status
    #def ask_to_join(group):
        #sends an notification to the group admin to allow a user to be added to group
