#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Initialize class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Define size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get area"""
        return (self.size * self.size)
