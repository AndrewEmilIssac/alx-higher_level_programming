#!/usr/bin/python3
""" square module"""

class Square:
    """define a square"""
    def _init_(self, size=0):
        if not isinstance(size, int):

            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size mist be >=0')
        self._size = size 
