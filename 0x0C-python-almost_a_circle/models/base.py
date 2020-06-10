#!/usr/bin/python3
"""module base
    """


import json
import turtle
import random
import csv


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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
        try:
            with open(cls.__name__ + ".json", mode="r") as data_file:
                text = data_file.read()
            text = cls.from_json_string(text)
            for item in text:
                if type(item) == dict:
                    array.append(cls.create(**item))
                else:
                    array.append(item)
            return array
        except:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """load fron file cvs
        """
        aux = []
        dict = {}
        with open(cls.__name__ + ".cvs", mode="r") as data_file:
            reader_from = csv.DictReader(data_file)
            for x in reader_from:
                for key, value in dict(x).items():
                    aux[key] = int(value)
                    aux.append(cls.create(dict))
        return aux

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file
        """
        aux = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as data_file:
            write = csv.DictWriter(data_file, aux[0].keys())
            write.writeheader()
            write.writerows(aux)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file
        """
        fieldnames = ["id", "width", "height", "x", "y"]
        aux = []
        try:
            with open(cls.__name__ + ".csv", mode="r") as data_file:
                read_from = csv.DictReader(data_file, fieldnames=fieldnames)
                for item in read_from:
                    aux_dict = {}
                    for k, v in dict(item).items():
                        aux_dict[k] = int(v)
                    print(item)
                    aux.append(cls.create(**aux_dict))
            return aux
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw shapes using the turtle module
        """
        colors_tortle = ["red", "purple", "black", "sienna", "orange"]
        colors_back = ["light yellow", "cornflower blue"]
        print(list_rectangles)
        print(list_squares)

        window = turtle.Screen()
        turtle.setup(1200, 800)
        window.bgcolor(random.choice(colors_back))
        window.title("Draws Turtle....")
        timmy = turtle.Turtle()
        turtle.shape("turtle")

        for var in list_rectangles + list_squares:
            turtle.color(random.choice(colors_tortle))
            turtle.pendown()
            turtle.fillcolor(random.choice(colors_tortle))
            turtle.begin_fill()
            for i in range(4):
                if i == 0 or i == 2:
                    turtle.forward(var.width)
                else:
                    turtle.forward(var.height)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(random.randint(-400, 200), random.randint(-400, 200))
        turtle.exitonclick()
