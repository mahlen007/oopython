#!/usr/bin/env python3
"""
Sortering methods
"""
def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

    return items

def recursive_insertion(items):
    """ Recursive insertion sort """