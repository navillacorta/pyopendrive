# -*- coding: utf-8 -*-

import requests
from pyopendrive.urls.urls import URLs




class BaseObject(dict):
    def __init__(self):
        self.DirUpdateTime = ''
        self.Name = ''
        self.ResponseType = ''
        self.Files = ''
        dict.__init__(self.__dict__)
{
    "DirUpdateTime": 1,
    "Name": "lib",
    "ResponseType": 1
}

{
    "DirUpdateTime": "1420695609",
    "Files": [
        {
            "Access": "0",
            "DateModified": "1420695599",
            "DateTrashed": "0",
            "DownloadLink": "https://www.opendrive.com/files/NzBfMzk4MDNfWktFTE5fNzk5NQ/test.txt",
            "Downloads": "0",
            "Extension": "txt",
            "FileGroupID": "0",
            "FileId": "NzBfMzk4MDNfWktFTE4",
            "Name": "test.txt",
            "Size": "0",
            "StreamingLink": "https://www.opendrive.com/files/NzBfMzk4MDNfWktFTE4/test.txt",
            "Views": "0"
        }
    ],
    "Name": "lib",
    "ResponseType": 1
}

