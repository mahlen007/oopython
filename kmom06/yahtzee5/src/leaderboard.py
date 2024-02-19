#!/usr/bin/env python3
"""
Class for Leaderboard
"""
import json
from src.unorderedlist import UnorderedList


class Leaderboard():
    """ class Leaderboard """
    def __init__(self, entries=None):
        self.entries=entries
        self.ul=UnorderedList()

    def save(self,filename):
        """ save to file method """
        json_object=[]
        for x in range(self.ul.size()):
            json_object.append(self.ul.get(x))

        with open(filename,'w', encoding='utf-8') as outfile:
            json.dump(json_object,outfile)
            #for x in range(self.ul.size()):
            #    file.write(f"{self.ul.get(x)}\n")#, {self.ul.get(x)[1]}\n")
        outfile.close()

    def load(self, filename):
        """ load from file method """
        # Open the file in read mode
        with open(filename, 'r', encoding='utf-8') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        for line in json_object:
            self.ul.append(line)
        openfile.close()
        #with open(filename, 'r', encoding='utf-8') as file:
        # Read all the lines of the file into a list
        #lines = file.readlines()
        #for line in lines:
        #    data=tuple(line.strip().split())
        #    print(data)
        #    self.ul.append(data)

    def add_entry(self, name, score):
        """ add entry to list method """
        self.ul.append((name,score))

    def remove_entry(self, index):
        """ remove entry from list method """
        data=self.ul.get(index)
        self.ul.remove(data)

if __name__ == "__main__":
    pass
