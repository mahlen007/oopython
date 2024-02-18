#!/usr/bin/env python3
"""
Class for Node in unorderedlist
"""
class Node:
    """ Class Node """
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def has_next(self):
        """ Checking if node has next """
        return self.next is not None

if __name__ == "__main__":
    pass
