#!/usr/bin/python3

def multiple_returns(sentence):
    """
    a function that returns a tuple with the
    length of a string and its first character
    """

    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
