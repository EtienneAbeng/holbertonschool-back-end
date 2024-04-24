#!/usr/bin/python3

import typing

def sum_mixed_list(mxd_lst: "typing.List[typing.Union[int, float]]") -> float:
    """ Return the sum of the list of floats and integers"""
    return sum(mxd_lst)