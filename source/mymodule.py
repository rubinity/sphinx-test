"""
MyModule: example module for Sphinx autodoc demo
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

def add(x, y):
    """
    Add two numbers.

    Parameters:
        x (int or float): first number
        y (int or float): second number

    Returns:
        int or float: sum of x and y
    """
    return x + y

def multiply(x, y):
    """
    Multiply two numbers.

    Parameters:
        x (int or float): first number
        y (int or float): second number

    Returns:
        int or float: product of x and y
    """
    return x * y
