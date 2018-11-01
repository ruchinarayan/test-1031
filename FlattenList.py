# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Coding Exercise 1: Flatten Nested List

"""
newflattenList = []
def flatten_list(nested_list):
    """
    Flatten an arbitrarily nested list

    Parameters
    ----------
    nested_list : nested list of int
        List with item to be either integers or list
        Example: [2,[[3,[4]], 5]]

    Returns
    -------
    flat_list : list of int
        A flattened list with only integers
        Example: [2,3,4,5]
    """
    for val in nested_list:
        if type(val) == list:
            flatten_list(val)
        else:
            newflattenList.append(val)
    return newflattenList
    
testList = [2,[[3,[4]], 5]]
#testList1 = ["This",[["is","a"], "Test"], "Value"]
#testList2 = ["This",[["0.00007","a", [10.2]], 10], "Value"]
print("A flattened list: ", flatten_list(testList))
#print("A flattened list: ", flatten_list(testList1))
#print("A flattened list: ", flatten_list(testList2))
