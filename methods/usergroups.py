import requests
from pyopendrive.urls.urls import URLs

class UserGroups(object):
    
    def list_all(self, session_id):
        headers = {'content-type': 'application/json'}
        params = {
            'session_id': session_id
            }
        
        try:
            r = requests.post(URLs.URL_USERGROUPS_ALL, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
