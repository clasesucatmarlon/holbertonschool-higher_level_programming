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
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write the json representation of a list of objects to a file
        task 16
        """
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as data_json:
                data_json.write(cls.to_json_string(None))
        else:
            array = []
            for obj in list_objs:
                array.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w+") as data_json:
                data_json.write(cls.to_json_string(array))

    @staticmethod
    def from_json_string(json_string):
        """
        return a list of diccionaries from json
        task 17
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attribites settarr
        task 18
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        task 19
        """
        array = []
        with open(cls.__name__ + ".json", mode="r") as data_file:
            text = data_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                array.append(cls.create(**item))
            else:
                array.append(item)
        return array
