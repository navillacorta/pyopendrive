import requests


        
        
"""
    def info(session, fileID):
        
        payload = {
            'session_id' : session.get("SessionID"),
            'file_id' : fileID
            }
"""



class OpenDrive(object):
    
    # API URLS
    
    ## SESSION
    URL_LOGIN = 'https://dev.opendrive.com/api/v1/session/login.json'
    URL_LOGOUT = 'https://dev.opendrive.com/api/v1/session/logout.json'
    
    ## FOLDER
    URL_FOLDER_LISTDIR = 'https://dev.opendrive.com/api/v1/folder/list.json'
    URL_FOLDER_GETPATH = 'https://dev.opendrive.com/api/v1/folder/path.json'
    URL_FOLDER_MKDIR = 'https://dev.opendrive.com/api/v1/folder.json'
    URL_FOLDER_MOVE_COPY = 'https://dev.opendrive.com/api/v1/folder/move_copy.json'
    URL_FOLDER_RENAME = 'https://dev.opendrive.com/api/v1/folder/rename.json'
    URL_FOLDER_RESTORE = 'https://dev.opendrive.com/api/v1/folder/restore.json'
    
    ## FILE
    URL_FILE_INFO = 'https://dev.opendrive.com/api/v1/file/info.json'
    URL_FILE_PATH = 'https://dev.opendrive.com/api/v1/file/path.json'
    URL_FILE_THUMB = 'https://dev.opendrive.com/api/v1/file/thumb.json'
    URL_FILE_ACCESS = 'https://dev.opendrive.com/api/v1/file/access.json'
    URL_FILE_ID_BY_PATH = 'https://dev.opendrive.com/api/v1/file/idbypath.json'

    # LIBRARY VERSION
    VERSION = '1'
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.SESSION_ACTIVE = False
    ## SESSION FUNCTIONS
    
    def login(self):
        payload = {
            'username' : self.username,
            'passwd' : self.password,
            'version' : self.VERSION
            }
        
        try:
            r = requests.post(self.URL_LOGIN, data=payload)
            if r.status_code is 200:
                self.session = r.json()
                self.SESSION_ACTIVE = True
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def session_exists(self):
        try:
            session_id = self.session["SessionID"]
            self.SESSION_ACTIVE = True
        except (NameError,AttributeError):
            print "You must login first"
            self.SESSION_ACTIVE = False
        except KeyError:
            print self.session["error"]["message"]
            self.SESSION_ACTIVE = False
        
        return self.SESSION_ACTIVE
    
    def logout(self):
        payload = {'session_id' : self.session['SessionID']}
        
        try:
            r = requests.post(self.URL_LOGOUT, data=payload)
            if r.status_code is 200:
                del self.session
                self.SESSION_ACTIVE = False
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    ## FILE FUNCTIONS
    
    def info(self, file_id):
        if not self.SESSION_ACTIVE:
            return None
        
        url = "%s/%s/%s" (
            self.URL_FILE_INFO,
            self.session["SessionID"],
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def path(self, file_id):
        if not self.SESSION_ACTIVE:
            return None
        
        url = "%s/%s/%s" (
            self.URL_FILE_PATH,
            self.session["SessionID"],
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def thumb(self, file_id):
        if not self.SESSION_ACTIVE:
            return None
        
        url = "%s/%s/%s" (
            self.URL_FILE_THUMB,
            self.session["SessionID"],
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def access(self, file_id, file_ispublic, access_folder_id):
        payload = {
            'session_id' : self.session["SessionID"],
            'file_id' : file_id,
            'file_ispublic' : file_ispublic,
            'access_folder_id' : access_folder_id
            }
        
        try:
            r = requests.post(self.URL_FILE_ACCESS, data=payload)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def id_by_path(self, file_id):
        payload = {
            'session_id' : self.session["SessionID"],
            'file_id' : file_id
            }
        
        try:
            r = requests.post(self.URL_FILE_ACCESS, data=payload)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def post(self, url, payload):
        try:
            r = requests.post(url, data=payload)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
    
    def move(self, file_id, dest_folder_id, overwrite_if_exists='false', src_access_folder_id, dst_access_folder_id):
        payload = {
            'session_id': self.session['SessionID'],
            'src_file_id': file_id,
            'dest_folder_id': dest_folder_id,
            'move': 'false',
            'overwrite_if_exists': overwrite_if_exists,
            }












o1 = OpenDrive(USERNAME, PASSWD)
o1.login()

