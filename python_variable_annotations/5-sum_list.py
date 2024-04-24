#!/usr/bin/python3

"""a type-annotated function sum_list which
takes a list input_list of floats as argument"""


def sum_list(input_list: "list[float]") -> float:
    """ Return the sum of the list of floats """
    return sum(input_list)
