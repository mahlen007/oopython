#!/usr/bin/env python3
"""
Sortering methods
"""
def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, items.size()):
        j = i
        while j > 0 and items.get(j) < items.get(j-1):
            temp=items.get(j)
            items.set(j,items.get(j-1))
            items.set(j-1,temp)
            #items[j], items[j-1] = items[j-1], items[j]
            j -= 1

    return items

def recursive_insertion(items, n):
    """ Recursive insertion sort """
    if n<=1:
        return items
    recursive_insertion(items, n-1)
    key=items.get(n-1)
    j=n-2
    while j>=0 and items.get(j)>key:
        items.set(j+1,items.get(j))
        j-=1
    items.set(j+1,key)
