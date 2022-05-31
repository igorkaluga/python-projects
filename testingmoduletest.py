#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:21:14 2022

@author: igororlov
"""

from doctest import run_docstring_examples

def add_ten(n):
    """
    Some function docstring here.
    
    >>> add_ten(10)
    20
    >>> add_ten(20)
    30
    """
    return n + 10

run_docstring_examples(add_ten, globals(), True)