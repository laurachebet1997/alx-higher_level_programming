#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Initialize class Square"""
    def __init__(self, size=0):
        """Init method of class Square"""
        self.size = size

    @property
    def size(self):
        """Define a size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Define a setter"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get area"""
        return (self.size * self.size)

    def my_print(self):
        """Print all"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
