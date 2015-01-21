# -*- coding: utf-8 -*-

import requests
from pyopendrive.urls.urls import URLs

        
        

class File(object):
    def info(self, session_id, file_id):
        url = "%s/%s/%s" (
            URLS.URL_FILE_INFO,
            session_id,
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def path(self, session_id, file_id):
        url = "%s/%s/%s" (
            URLs.URL_FILE_PATH,
            session_id,
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def thumb(self, session_id, file_id):
        url = "%s/%s/%s" (
            URLs.URL_FILE_THUMB,
            session_id,
            file_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def access(self, session_id, file_id, file_ispublic=0, access_folder_id=''):
        params = {
            'session_id' : session_id,
            'file_id' : file_id,
            'file_ispublic' : file_ispublic,
            'access_folder_id' : access_folder_id
            }
        
        try:
            r = requests.post(URLs.URL_FILE_ACCESS, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def id_by_path(self, session_id, file_id):
        params = {
            'session_id' : session_id,
            'file_id' : file_id
            }
        
        try:
            r = requests.post(URLs.URL_FILE_ACCESS, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def move(self, session_id, file_id, dest_folder_id, overwrite_if_exists='false'):
        params = {
            'session_id': session_id,
            'src_file_id': file_id,
            'dest_folder_id': dest_folder_id,
            'move': 'true',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = requests.post(URLs.URL_FILE_MOVE_COPY, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def copy(self, session_id, file_id, dest_folder_id, overwrite_if_exists='false'):
        params = {
            'session_id': session_id,
            'src_file_id': file_id,
            'dest_folder_id': dest_folder_id,
            'move': 'false',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = requests.post(URLs.URL_FILE_MOVE_COPY, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise

    

