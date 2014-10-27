#/v1/upload/close_file_upload.json
"""Implementation Notes:
Close file upload should be called after file upload

Parameters:

    REQUEST_BODY:
        Object{
            "session_id": "",
            "file_id": "",
            "temp_location": "",
            "file_size": "",
            "file_time": "",
            "access_folder_id": ""
            } 	
        
        
    session_id : string (required) - Session ID.
    file_id : string (required) - File ID.
    temp_location : string (required) - File temp location.file_size : int (required) - File size in bytes.
    file_time : int - Time of file creation.
    access_folder_id : string - Access folder ID.
"""


#/v1/upload/create_file.json
"""Implementation Notes:
Create file should be called before file upload

Parameters:

    REQUEST_BODY:
        Object{ "session_id": "",
        "folder_id": "",
        "file_name": "",
        "file_size": "",
        "access_folder_id": ""
        }

    session_id : string (required) - Session ID.
    folder_id : string (required) - Folder ID.
    file_name : string (required) - File Name.
    file_size : string (required) - File Size in bytes.
    access_folder_id : string - Access folder ID.
"""


#/v1/upload/open_file_upload.json
"""Implementation Notes:
Open file upload should be called before file upload

Parameters:

    REQUEST_BODY:
        Object{
            "session_id": "",
            "file_id": "",
            "file_size": "",
            "access_folder_id": ""
            } 	

    session_id : string (required) - Session ID.
    file_id : string (required) - File ID.
    file_size : int (required) - File Size.
    access_folder_id : string - Access folder ID.
"""





























