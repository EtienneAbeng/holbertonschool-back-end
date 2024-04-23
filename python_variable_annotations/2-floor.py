#!/usr/bin/python3

""" A type-annotated function floor that takes a float n as argument and returns the floor of the float """

import math  # import the math module


def floor(n: int | float) -> int:  # type hinting
    """ Return the floor of the float """
    return math.floor(n)
