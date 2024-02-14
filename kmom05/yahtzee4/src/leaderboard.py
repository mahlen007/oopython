#!/usr/bin/env python3
"""
Class for Leaderboard
"""
from src.unorderedlist import UnorderedList

class Leaderboard():
    def __init__(self, entries=None):
        self.entries=entries
    
    def save(self,filename):
        items = ['Mango', 'Orange', 'Apple', 'Lemon']
        file = open(filename,'w')
        for the item in items:
	        file.write(item+"\n")
        file.close()
    
    def load(self, filename):
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all the lines of the file into a list
            lines = file.readlines()
    
    def add_entry(self, name, score):
        pass
    
    def remove_entry(self, index):
        pass