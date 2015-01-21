# -*- coding: utf-8 -*-

class BaseError(Exception):
    def __init__(self, *args, **kwargs):
        if "message" in kwargs:
            self.message = kwargs.get("message")
        Exception.__init__(self, *args)
    
    def __str__(self):
        return " ".join([self.args[0], self.message])


class ValidationError(BaseError):
    pass    

