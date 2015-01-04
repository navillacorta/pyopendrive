# -*- coding: utf-8 -*-

import requests
from URLs import URLs

        
        

class File(object):
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
            raise
    
    def move(self, file_id, dest_folder_id, overwrite_if_exists='false'):
        payload = {
            'session_id': self.session['SessionID'],
            'src_file_id': file_id,
            'dest_folder_id': dest_folder_id,
            'move': 'true',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = self.post(self.URL_FILE_MOVE_COPY, payload)
            return r
        except:
            return None
    
    def copy(self, file_id, dest_folder_id, overwrite_if_exists='false'):
        payload = {
            'session_id': self.session['SessionID'],
            'src_file_id': file_id,
            'dest_folder_id': dest_folder_id,
            'move': 'false',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = self.post(self.URL_FILE_MOVE_COPY, payload)
            return r
        except:
            return None

    

