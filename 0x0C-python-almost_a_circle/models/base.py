#!/usr/bin/python3
''' models/base.py
'''
import os
import re
from random import randint
from json import JSONDecoder, JSONEncoder


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

    @classmethod
    def load_from_file(cls):
        """Loads a list of polygons from a file in JSON format.
        Returns:
            list: A list of polygons.
        """
        file_name = '{}.json'.format(cls.__name__)
        lines = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    lines.append(line)
        txt = ''.join(lines)
        attr_dicts = cls.from_json_string(txt)
        cls_list = list(map(lambda x: cls.create(**x), attr_dicts))
        return cls_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of polygons to a file in CSV format.
        Args:
            list_objs (list): A list of polygons.
        """
        file_name = '{}.csv'.format(cls.__name__)
        poly_fmt_fxns = {
            'Rectangle': lambda x: '{},{:d},{:d},{:d},{:d}'.format(
                x.id, x.width, x.height, x.x, x.y),
            'Square': lambda x: '{},{:d},{:d},{:d}'.format(
                x.id, x.size, x.x, x.y),
        }
        vals_list = []
        if list_objs is not None:
            poly_name = cls.__name__
            for obj in list_objs:
                if (type(obj) is cls) and (poly_name in poly_fmt_fxns):
                    vals_list.append('{}\n'.format(
                        poly_fmt_fxns[poly_name](obj)))
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.writelines(vals_list)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of polygons from a file in CSV format.
        Returns:
            list: A list of polygons.
        """
        poly_name = cls.__name__
        file_name = '{}.csv'.format(poly_name)
        poly_fmt_fxns = {
            'Rectangle': lambda x: {
                'id': int(x[0]),
                'width': int(x[1]),
                'height': int(x[2]),
                'x': int(x[3]),
                'y': int(x[4]),
            },
            'Square': lambda x: {
                'id': int(x[0]),
                'size': int(x[1]),
                'x': int(x[2]),
                'y': int(x[3]),
            },
        }
        poly_fmt = {
            'Rectangle': r'\s*[^,]+,[^,]+,[^,]+,[^,]+,[^,]+',
            'Square': r'\s*[^,]+,[^,]+,[^,]+,[^,]+',
        }
        lines = []
        attr_dicts = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    attrs_match = re.match(poly_fmt[poly_name], line)
                    if attrs_match is not None:
                        cols = line.strip().split(',')
                        attr_dicts.append(poly_fmt_fxns[poly_name](cols))
        cls_list = list(map(lambda x: cls.create(**x), attr_dicts))
        return cls_list
