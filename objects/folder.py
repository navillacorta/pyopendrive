# -*- coding: utf-8 -*-

from pyopendrive.objects.base import BaseObject
from pyopendrive.exceptions import ValidationError
import pyopendrive.methods.folder

import os

class FolderObject(BaseObject,pyopendrive.methods.folder.Folder):
    
    def __init__(self, **kwargs):
        for key in kwargs:
            try:
                self.__dict__['_'+key] = kwargs.get(key)
            except:
                continue
        
    def _set_dir_path(self, path):
        self._folder_path = path
        
    def _set_folder_name(self, folder_name):
        self._folder_name = os.path.basename(folder_name)
    
    def _set_sub_parent_id(self, sub_parent_id):
        self._sub_parent_id = sub_parent_id
    
    def _set_dir_update_time(self, dir_update_time):
        self._dir_update_time = dir_update_time
    
    def _set_folder_id(self, folder_id):
        self._folder_id = folder_id
    
    def validate(self):
        try:
            for key in ["_session_id", "_folder_name", "_sub_parent_id", "_access"]:
                try:
                    if not self.__dict__[key]:
                        raise ValidationError(key, message="not valid")
                except KeyError:
                    raise ValidationError(key, message="not set")
        except:
            raise
    
    def init(self):
        try:
            try:
                self.validate()
            except ValidationError, e:
                print e
                return False
                
            self._opendrive_folder = self.create(
                self._session_id,
                self._folder_name,
                self._sub_parent_id,
                self._access
                )
            
            self.set_folder_data()
        except:
            raise
    
    def set_folder_data(self):
        try:
            self._set_folder_id(self._opendrive_folder.get("FolderID"))
            self._set_dir_update_time(self._opendrive_folder.get("DirUpdateTime"))
        except:
            raise
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
