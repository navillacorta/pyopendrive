# -*- coding: utf-8 -*-

import requests
import pyopendrive.methods.upload
from pyopendrive.urls.urls import URLs

import time
import os

class UploadObject(pyopendrive.methods.upload.Upload):
    def __init__(self, srcFile, session_id, bs=131072, root_dir=0):
        self._src_file = srcFile
        self._session_id = session_id
        self._root_dir = root_dir
        self._bs = bs
        
        self._src_basename = os.path.basename(self._src_file)
        self._src_size = os.path.getsize(self._src_file)
        self._bytes_seen = 0
        self._bytes_sent = 0
        self._file_io = self._open_src_file()
    
    def _open_src_file(self):
        self._file = open(self._src_file, 'rb')
        while 1:
            self._buf = self._file.read(self._bs)
            if not self._buf:
                return
            else:
                self._bytes_seen += len(self._buf)
                yield self._buf
    
    def _set_session_id(self, session_id):
        self._session_id = session_id
    
    def init_file(self):
        try:
            self._opendrive_file = self.create_file(self._session_id, self._root_dir, self._src_basename, self._src_size)
        except:
            raise
    
    def init_temp_file(self):
        try:
            self._opendrive_temp_file = self.open_file(self._session_id,  self._opendrive_file.get("FileId"), self._src_size)
        except:
            raise
    
    def run(self):
            for data in self._file_io:
                result = self.file_chunk(self._session_id, self._opendrive_file.get("FileId"), self._opendrive_temp_file.get("TempLocation"), self._bytes_sent, len(data), data)
                
                try:
                    self._bytes_sent += int(result.get("TotalWritten"))
                    yield self._bytes_sent
                except:
                    raise
    
    
    def close(self):
        try:
            self._opendrive_closed_file = self.close_file_upload(self._session_id, self._opendrive_file.get("FileId"), self._opendrive_temp_file.get("TempLocation"), self._src_size, int(os.stat(self._src_file).st_mtime))
        except:
            raise


