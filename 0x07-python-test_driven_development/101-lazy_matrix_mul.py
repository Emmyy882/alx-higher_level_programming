#!/usr/bin/python3
""" Numpy Module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    # Write a function that multiplies 2 matrices by using the module NumPy...
    # Test cases should be the same as 100-matrix_mul but with....
    # new exception type/message
    # VARIABLE(" "):
    # Lazy_Numpy: Lazy matrix multiplication
    # Return: Always 0. (Success).
    """
    return numpy.matmul(m_a, m_b)
