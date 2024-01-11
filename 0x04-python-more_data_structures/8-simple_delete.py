#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new = list(a_dictionary)
    for i in new:
        if i == key:
            del(a_dictionary[i])
    return a_dictionary
