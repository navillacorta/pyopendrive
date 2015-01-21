# -*- coding: utf-8 -*-

class URLs(object):
    # API URLS
    
    ## SESSION
    URL_SESSION_LOGIN = 'https://dev.opendrive.com/api/v1/session/login.json'
    URL_SESSION_LOGOUT = 'https://dev.opendrive.com/api/v1/session/logout.json'
    URL_SESSION_EXISTS = 'https://dev.opendrive.com/api/v1/session/exists.json'
    
    ## FOLDER
    URL_FOLDER_LIST = 'https://dev.opendrive.com/api/v1/folder/list.json'
    URL_FOLDER_PATH = 'https://dev.opendrive.com/api/v1/folder/path.json'
    URL_FOLDER_FOLDER = 'https://dev.opendrive.com/api/v1/folder.json'
    URL_FOLDER_ID_BY_PATH = 'https://dev.opendrive.com/api/v1/folder/idbypath.json'
    URL_FOLDER_MOVE_COPY = 'https://dev.opendrive.com/api/v1/folder/move_copy.json'
    URL_FOLDER_REMOVE = 'https://dev.opendrive.com/api/v1/folder/remove.json'
    URL_FOLDER_RENAME = 'https://dev.opendrive.com/api/v1/folder/rename.json'
    URL_FOLDER_RESTORE = 'https://dev.opendrive.com/api/v1/folder/restore.json'
    URL_FOLDER_SET_ACCESS = 'https://dev.opendrive.com/api/v1/folder/setaccess.json'
    URL_FOLDER_TRASH = 'https://dev.opendrive.com/api/v1/folder/trash.json'
    URL_FOLDER_DELETE = 'https://dev.opendrive.com/api/v1/folder/trash.json'
    
    ## FILE
    URL_FILE_INFO = 'https://dev.opendrive.com/api/v1/file/info.json'
    URL_FILE_PATH = 'https://dev.opendrive.com/api/v1/file/path.json'
    URL_FILE_THUMB = 'https://dev.opendrive.com/api/v1/file/thumb.json'
    URL_FILE_ACCESS = 'https://dev.opendrive.com/api/v1/file/access.json'
    URL_FILE_ID_BY_PATH = 'https://dev.opendrive.com/api/v1/file/idbypath.json'
    URL_FILE_MOVE_COPY = 'https://dev.opendrive.com/api/v1/file/move_copy.json'
    URL_FILE_RENAME = 'https://dev.opendrive.com/api/v1/file/rename.json'
    URL_FILE_RESTORE = 'https://dev.opendrive.com/api/v1/file/restore.json'
    URL_FILE_TRASH = 'https://dev.opendrive.com/api/v1/file/trash.json'
    URL_FILE_DELETE = 'https://dev.opendrive.com/api/v1/file.json'
    
    # UPLOAD    
    URL_UPLOAD_CLOSE_FILE = 'https://dev.opendrive.com/api/v1/upload/close_file_upload.json'
    URL_UPLOAD_CREATE_OPEN = 'https://dev.opendrive.com/api/v1/upload/create_file.json'
    URL_UPLOAD_OPEN = 'https://dev.opendrive.com/api/v1/upload/open_file_upload.json'
    URL_UPLOAD_RESUMABLE = 'https://dev.opendrive.com/api/v1/upload/resumable.json'
    URL_UPLOAD_FILE_CHUNK = 'https://dev.opendrive.com/api/v1/upload/upload_file_chunk.json'


    # ACCOUNTUSERS
    URL_ACCOUNTUSERS_INFO = 'https://dev.opendrive.com/api/v1/accountusers/info.json'
    URL_ACCOUNTUSERS_USERS_IN_GROUP = 'https://dev.opendrive.com/api/v1/accountusers/usersingroup.json'
    URL_ACCOUNTUSERS_ACCOUNT_USERS = 'https://dev.opendrive.com/api/v1/accountusers.json'
    URL_ACCOUNTUSERS_MOVE = 'https://dev.opendrive.com/api/v1/accountusers/move.json'
    URL_ACCOUNTUSERS_SET_ACCESS = 'https://dev.opendrive.com/api/v1/accountusers/setaccess.json'
    URL_ACCOUNTUSERS_SET_FOLDER_ACCESS = 'https://dev.opendrive.com/api/v1/accountusers/setfolderaccess.json'
    
    # USER GROUPS
    URL_USERGROUPS_ALL = 'https://dev.opendrive.com/api/v1/usergroups/all.json'
    URL_USERGROUPS_USER_GROUPS = 'https://dev.opendrive.com/api/v1/usergroups.json'

    # USER
    URL_USERS_INFO = 'https://dev.opendrive.com/api/v1/users/info.json'
    URL_USERS_FORGOT_PASSWORD = 'https://dev.opendrive.com/api/v1/users/forgotpassword.json'
    URL_USERS_VERIFY_EMAIL = 'https://dev.opendrive.com/api/v1/users/verifyemail.json'
    URL_USERS_EMAIL = 'https://dev.opendrive.com/api/v1/users/email.json'
    URL_USERS_PASSWORD = 'https://dev.opendrive.com/api/v1/users/password.json'
    URL_USERS_USER_NAME = 'https://dev.opendrive.com/api/v1/users/username.json'

