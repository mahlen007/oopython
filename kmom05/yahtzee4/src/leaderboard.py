#!/usr/bin/env python3
"""
Class for Leaderboard
"""
from unorderedlist import UnorderedList

class Leaderboard():
    """ class Leaderboard """
    def __init__(self, entries=None):
        self.entries=entries
        self.ul=UnorderedList()
        
    
    def save(self,filename):
        """ save to file method """
        file = open(filename,'w')
        for x in range(self.ul.size()):
	        file.write(str(self.ul.get(x))+"\n")
        file.close()
    
    def load(self, filename):
        """ load from file method """
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all the lines of the file into a list
            lines = file.readlines()
    
    def add_entry(self, name, score):
        """ add entry to list method """
        self.ul.append((name,score))
    
    def remove_entry(self, index):
        """ remove entry from list method """
        data=self.ul.get(index)
        self.ul.remove(data)

if __name__ == "__main__":
    lb=Leaderboard()
    lb.add_entry("Mattias",100)
    lb.add_entry("Bo",70)
    lb.add_entry("Bengt",110)
    lb.remove_entry(2)
    lb.save("test.txt")
