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

project_list = api(path = '/projects')

for each_project in project_list['items']:
	member_path = '/projects/' + each_project['id'] + '/members'
	member_list = api(path = member_path)
	for each_member in member_list['items']:
		print 'USER:' + each_member['username'] + '\tPROJECT: ' + each_project['id'] + '\tPERMISSIONS: ' +str(each_member['permissions'])
