# -*- coding: utf-8 -*-

class BaseValueError(ValueError):
    def __init__(self, message, description, *args, **kwargs):
        self.message = message
        self.description = description
        super(BaseError, self).__init__(message, description, *args, **kwargs) 

