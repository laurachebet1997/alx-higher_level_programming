#!/usr/bin/python3
''' models/base.py
'''
import json


class Base:
    ''' first class Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize Base  __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        '''method: save_to_file
        '''
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                tmp_dict = cls.to_dictionary(obj)
                list_dicts.append(tmp_dict)
            json_L_of_D = cls.to_json_string(list_dicts)
        else:
            json_L_of_D = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            num_char = file.write(json_L_of_D)

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' method json string
        '''
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)

    @staticmethod
    def from_json_string(json_string):
        """Creates a list from its JSON representation.
        Args:
            json_string (str): A JSON string representation of a list.
        Returns:
            list: A JSON representation of the list of dictionaries.
        """
        if (json_string is None) or (len(json_string.strip()) == 0):
            return []
        else:
            return JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a polygon with the given attributes.
        Args:
            dictionary (dict): A dictionary of the object's attributes.
        Returns:
            Base: A polygon object with the given attributes.
        """
        polygons = {
            'Rectangle': (1, 1, 0, 0, None),
            'Square': (1, 0, 0, None),
        }
        if cls.__name__ in polygons.keys():
            polygon = cls(*polygons[cls.__name__])
            polygon.update(**dictionary)
            return polygon
