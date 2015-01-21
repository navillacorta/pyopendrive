# -*- coding: utf-8 -*-

import requests
from pyopendrive.urls.urls import URLs

        
        

class Folder(object):
    def list(self, session_id, folder_id):
        url = "%s/%s/%s" % (
            URLs.URL_FOLDER_LIST,
            session_id,
            folder_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def path(self, session_id, folder_id):
        url = "%s/%s/%s" % (
            URLs.URL_FOLDER_PATH,
            session_id,
            folder_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def thumb(self, session_id, folder_id):
        url = "%s/%s/%s" % (
            URLs.URL_FOLDER_THUMB,
            session_id,
            folder_id
            )
        
        try:
            r = requests.get(url)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def access(self, session_id, folder_id, file_ispublic=0, access_folder_id=''):
        params = {
            'session_id' : session_id,
            'folder_id' : folder_id,
            'file_ispublic' : file_ispublic,
            'access_folder_id' : access_folder_id
            }
        
        try:
            r = requests.post(URLs.URL_FOLDER_ACCESS, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def id_by_path(self, session_id, path):
        params = {
            'session_id' : session_id,
            'path' : path
            }
        
        try:
            r = requests.post(URLs.URL_FOLDER_ID_BY_PATH, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def move(self, session_id, folder_id, dest_folder_id, overwrite_if_exists='false'):
        params = {
            'session_id': session_id,
            'src_folder_id': folder_id,
            'dest_folder_id': dest_folder_id,
            'move': 'true',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = requests.post(URLs.URL_FOLDER_MOVE_COPY, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def copy(self, session_id, folder_id, dest_folder_id, overwrite_if_exists='false'):
        params = {
            'session_id': session_id,
            'src_folder_id': folder_id,
            'dest_folder_id': dest_folder_id,
            'move': 'false',
            'overwrite_if_exists': overwrite_if_exists,
            }
        
        try:
            r = requests.post(URLs.URL_FOLDER_MOVE_COPY, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def create(self, session_id, folder_name, folder_sub_parent, folder_ispublic=0):
        params = {
            'session_id': session_id,
            'folder_name': folder_name,
            'folder_sub_parent': folder_sub_parent,
            'folder_ispublic': folder_ispublic
            }
        
        try:
            r = requests.post(URLs.URL_FOLDER_FOLDER, data=params)
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
    def _iter_path(self, order="descending"):
        tree = []
        dir_path = os.path.dirname(self.srcfile)
        
        while 1:
            p = os.path.dirname(dir_path)
            
            if p == "/":
                break
                
            tree.append(os.path.basename(p))
            dir_path = p
        
        if order == "ascending":
            pass
        elif order == "descending":
            tree.reverse()
        
        for d in tree:
            yield d

