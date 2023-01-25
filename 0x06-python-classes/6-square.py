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

    @property
    def position(self):
        '''Retrieves the position of this Square.
        Returns:
            tuple: The position of this Square.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Updates the position of this Square.
        Args:
            value (tuple): The new position of this Square.
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        """Get area"""
        return (self.size * self.size)

    def my_print(self):
        '''Prints a 2D table of the '#' symbol with the size of this square
        based on its position.
        '''
        if self.size == 0:
            print('')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))
