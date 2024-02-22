#!/usr/bin/env python3
"""
Class for Queue
"""
from src.die import Die

class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        """ Check if queue is empty """
        return self._items == []

    def enqueue(self, item):
        """ Append item to queue """
        self._items.append(item)

    def dequeue(self):
        """ Remove item from queue """
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        """ Check next item in queue, without take it away """
        return self._items[0]

    def to_list(self):
        """ Return a list from the queue """
        my_list=[]
        for item in self._items:
            my_list.append(item.dequeue())
        return my_list

    def from_list(self,my_list):
        """ Fill the queue from a list """
        for item in my_list:
            self.enqueue(item)

    def size(self):
        """ Number of items in queue """
        return len(self._items)
