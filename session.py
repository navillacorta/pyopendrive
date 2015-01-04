# -*- coding: utf-8 -*-


import requests
from URLs import URLs

class Session(object):
    def __init__(self):
        pass
    
    def exists(self, session_id=''):
        if not session_id:
            session_id=self.SessionID
        
        payload = {
            'session_id' : session_id
            }

        try:
            r = requests.post(URLs.URL_SESSION_EXISTS, data=payload)
            if r.status_code is 200:
                return True
            if r.status_code is 401:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
            return

    def login(self, username='', password=''):
        if username:
            self.set_username(username)
        else:
            username = self.UserName
        
        if password:
            self.set_password(password)
        else:
            password = self.Password
        
        payload = {
            'username' : username,
            'passwd' : password,
            'version' : 1
            }

        try:
            r = requests.post(URLs.URL_SESSION_LOGIN, data=payload)
            if r.status_code is 200:
                self.set_session_data(r.json())
                self.json = r.json()
                return True
            
            if r.status_code is 401:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
            return
    
    def logout(self, session_id=''):
        if not session_id:
            session_id=self.SessionID
        
        payload = {
            'session_id' : session_id
            }

        try:
            r = requests.post(URLs.URL_SESSION_LOGOUT, data=payload)
            if r.status_code is 200:
                del self.SessionID
            if r.status_code is 400:
                r.raise_for_status()
        except requests.HTTPError, e:
            print e
            return False
        
        return True
    
    def set_session_id(self, session_id):
        self.SessionID = session_id

    def set_password(self, passwd):
        self.Password = passwd

    def set_username(self, username):
        self.UserName = username
    
    def set_user_first_name(self, user_first_name):
        self.UserLastName = user_first_name

    def set_user_last_name(self, user_last_name):
        self.UserLastName = user_last_name

    def set_acc_type(self, acc_type):
        self.AccType = acc_type
    
    def set_user_lang(self, user_lang):
        self.UserLang = user_lang

    def set_access_user(self, access_user):
        self.IsAccessUser = access_user

    def set_drive_name(self, drive_name):
        self.DriveName = drive_name
    
    def set_encoding(self, encoding):
        self.Encoding = encoding
    
    def set_session_data(self, data):
        try:
            self.set_session_id(data.get("SessionID"))
            self.set_password(self.Password)
            self.set_username(data.get("UserName"))
            self.set_user_first_name(data.get("UserFirstName"))
            self.set_user_last_name(data.get("UserLastName"))
            self.set_acc_type(int(data.get("AccType")))
            self.set_user_lang(data.get("UserLang"))
            self.set_access_user(int(data.get("IsAccessUser")))
            self.set_drive_name(data.get("DriveName"))
            self.set_encoding(data.get("Encoding"))
            
            return True
        except Exception, e:
            print e
            return False

