#!/usr/bin/python3
'''Base class module - tests located in test/test_base.py'''
from json import dumps
from json import loads
import csv


class Base:
    '''the Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init magic'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
