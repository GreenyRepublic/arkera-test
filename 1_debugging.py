from unittest import TestCase

def increment_dictionary_values (d, i):
    newDict = {}
    for k, v in d.items():
        newDict[k] = v + i
    return newDict