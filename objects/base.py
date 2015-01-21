# -*- coding: utf-8 -*-

class BaseObject(object):
    
    def _set_session_id(self, session_id):
        self._session_id = session_id
    
    def _set_folder_access(self, val):
        self._access = val
    
    def is_private(self):
        if self._access is 0:
            return True
        else:
            return False
    
    def is_public(self):
        if self._access is 1:
            return True
        else:
            return False
    
    def is_hidden(self):
        if self._access is 2:
            return True
        else:
            return False
