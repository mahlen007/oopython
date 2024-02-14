#!/usr/bin/env python3
"""
Class for Unorderedlist
"""
from node import Node
from exceptions import MissingIndex
from exceptions import MissingValue

class UnorderedList():
    """ Class Unordered List """
    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, value):
        """ append method """
        tmp = Node(value)
        if self._head is None:
            self._head = tmp
        else:
            current = self._head
            while current.has_next():
                current = current.next
            current.next = tmp

    def get(self,index):
        """ get method """
        current=self._head
        ind=0
        if current is None:
            return -1
        while current.has_next() and ind<index:
            ind+=1
            current = current.next
        if ind==index:
            return current.value
        return -1

    def set(self,index,data):
        """ set method """
        current=self._head
        ind=0
        if current is None:
            return -1
        while current.has_next() and ind<index:
            ind+=1
            current = current.next
        if ind==index:
            current.value=data
            return
        return -1

    def index_of(self, data):
        """ index of method """
        current=self._head
        ind=0
        if current.value==data:
            return ind
        while current.has_next():
            ind+=1
            if current.value==data:
                return ind
            current = current.next
        return -1    

    def remove(self, data):
        """ remove method """
        current=self._head
        if current.value==data:
            self._head=current.next
            return
        
        while current is not None:
            if current.value==data:
                break
            previous=current
            current=current.next
            #print(str(previous.value)+"  "+str(current.value))
        
        if current is None:
            return -1
        
        previous.next=current.next
        return

    # def remove(self, data):
    #     """ remove method """
    #     current=self._head
    #     if current.value==data:
    #         self._head=current.next
    #         return
    #     previous=current
    #     while current.has_next() and not current.value==data:
    #         previous=current
    #         current=current.next
    #         print(str(previous.value)+"  "+str(current.value))
    #     if current.value==data:
    #         previous=current.next
    #         print(previous.value)
    #         return
    #     return -1   

    def size(self):
        """ size method """
        current=self._head
        ind=0
        if current is None:
            return 0
        ind+=1
        while current.has_next():
            ind+=1
            current = current.next
        return ind    

    def print_list(self):
        """ print method """
        current = self._head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    ul = UnorderedList()
    ul.append(10)
    ul.append("hej")
    ul.append(1)
    #treevizer.to_png(ul._head, "ll")
    ul.append(3)
    ul.print_list()
    ul.remove(10)
    ul.print_list()
    ul.remove(1)
    ul.print_list()
    ul.remove(3)
    ul.print_list()
