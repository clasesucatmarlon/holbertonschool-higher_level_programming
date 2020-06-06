#!/usr/bin/python3
"""module base
    """


import json


class Base:
    """Base class with methods
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation of list of directories

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as data_json:
                data_json.write(cls.to_json_string(None))
        else:
            array = []
            for obj in list_objs:
                array.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w+") as data_json:
                data_json.write(cls.to_json_string(array))
