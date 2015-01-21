# -*- coding: utf-8 -*-

import requests
import json
from pyopendrive.urls.urls import URLs

class Upload(object):
	
    def close_file_upload(self, session_id, file_id, temp_location, file_size, file_time, access_folder_id=""):
        """Method:
    Post
Post Parameters:
    session_id : string (required) - Session ID.
    access_folder_id : string – Access folder ID.
    file_id : string (required) - File ID.
    temp_location : string (required) – File temp location.
    file_time : int eger (required) – Time of file creation.
    file_size : int eger (required) - File size in bytes.

Returns:
    DirUpdateTime:
        integer (10). Directory update time.
    Errors:
        400: Bad Request: Invalidfile ID
        400: Bad Request: invalid value specified for `file_size`. Expecting integer value
        401: Unauthorized: Session has expired. Please right click on OpenDrive task bar icon, log out and then log back in."""
        
        payload = {
            "session_id": session_id,
            "file_id": file_id,
            "temp_location": temp_location,
            "file_size": file_size,
            "file_time": file_time,
            "access_folder_id": access_folder_id
            }
        
        headers = {'content-type': 'application/json'}
        
        try:
            r = requests.post(URLs.URL_UPLOAD_CLOSE_FILE, headers=headers, data=json.dumps(payload))
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise    
    
    def create_file(self, session_id, folder_id, file_name, file_size, **kwargs):
        """Method:
    Post

Parameters:
    session_id: string (required) - Session ID.
    access_folder_id: string – Access folder ID.
    folder_id: string (required) - Folder ID.
    file_name: string (required) - File name.
    file_size: string (required) - File size in bytes.
    open_existing: string (required) - (true, false).

Returns:
    FileId: String. The files Id.
    DirUpdateTime: Integer (10). The directory update time.

Errors:
    400: Bad Request: Invalid file ID
    401: Unauthorized: Session has expired. Please right click on OpenDrive task bar icon, log out and then log back in.

Notes:
    Create file should be called before upload."""
        
        payload = {
            "session_id": session_id,
            "folder_id": folder_id,
            "file_name": file_name,
            "file_size": file_size,
            }
        payload = dict(payload.items() + kwargs.items())
        
        headers = {'content-type': 'application/json'}
        
        try:
            r = requests.post(URLs.URL_UPLOAD_CREATE_OPEN, headers=headers, data=json.dumps(payload))
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            print r


    def open_file(self, session_id, file_id, file_size, access_folder_id=""):
        """Method:
    Post

Parameters:
    session_id: string (required) - Session ID.
    access_folder_id: string – Access folder ID.
    file_id: string (required)- File ID.
    file_size: integer (required) - File size in bytes.

Returns:
    TempLocation: String. The temporary file storage location prior to it going to its assigned folder.

Errors:
    400: Bad Request: Invalid file ID
    401: Unauthorized: Session has expired. Please right click on OpenDrive task bar icon, log out and then log back in.

Notes:
    Open file upload should be called before file upload."""
        
        payload = {
            "session_id": session_id,
            "file_id": file_id,
            "file_size": file_size,
            "access_folder_id": access_folder_id
            }
        
        headers = {'content-type': 'application/json'}
        
        try:
            r = requests.post(URLs.URL_UPLOAD_OPEN, headers=headers, data=json.dumps(payload))
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise
    
                
    def file_chunk(self, session_id, file_id, temp_location, chunk_offset, chunk_size, data, access_folder_id=""):
        """Method:
    Post

Parameters:
    session_id: string (required) - Session ID.
    access_folder_id: string – Access folder ID.
    file_id: string (required) - File ID.
    temp_location: string (required) – File temporary location.
    chunk_offset:integer (required) – Size of chunk offset in bytes.
    chunk_size: integer (required) – Chunk size in bytes.

Returns:
    TotalWritten: Integer. File size in bytes.

Errors:
    400: Bad Request: Invalid file ID
    401: Unauthorized: Session has expired. Please right click on OpenDrive task bar icon, log out and then log back in.
    404: Not Found: Could not open chunk on server."""
        
        payload = {
            "session_id" : session_id, 
            "file_id" : file_id, 
            "temp_location" : temp_location, 
            "chunk_offset" : chunk_offset, 
            "chunk_size" : chunk_size
            }
        
        #headers = {'content-type': 'application/json'}
        
        try:
            r = requests.post(URLs.URL_UPLOAD_FILE_CHUNK, data=payload, files={'file_data': data})
            if r.status_code is 200:
                return r.json()
            else:
                r.raise_for_status()
        except:
            raise



