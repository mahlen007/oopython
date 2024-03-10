#!/usr/bin/env python3
"""
Class for Trie
"""
from src.node import Node
#from src.errors import MissingIndex
#from src.errors import MissingValue

class Trie():
    """ Class Trie """
    def __init__(self):
        self.root=Node()

    def has_child(self,node):
        for i in range(26):
            if node.children[i]:
                return True
        return False

    def insert(self, word):
        """ Insert a word in the trie """
        current = self.root
        for letter in word:
            index=ord(letter)-ord('a')
            if not current.children[index]:
                current.children[index]=Node()
            current=current.children[index]
        current.isEndOfWord=True

    def search(self, word):
        """ Search for a word in the trie """
        current=self.root
        for letter in word:
            index=ord(letter)-ord('a')
            if not current.children[index]:
                return False
            current=current.children[index]
        return current.isEndOfWord==True

    def insert_from_list(self,list_word):
        """ read from a list and insert """
        for word in list_word:
            self.insert(word)

    def read_from_file(self,filename):
        list_=[]
        with open(filename, 'r', encoding='utf-8') as openfile:
            # Reading from json file
            #json_object = json.load(openfile)
            for line in openfile:
                list_.append(line.strip())
        openfile.close()
        return list_


    def get(self,index):
        """ get method """


    def set(self,index,data):
        """ set method """

    def index_of(self, data):
        """ index of method """

    def remove(self, data):
        """ remove method """

    def word_count(self,node):
        """ size method """
        result=0
        if node.isEndOfWord is True:
            result += 1
        for x in range(26):
            if node.children[x] is not None:
                result += self.word_count(node.children[x])
        return result

    def print_list(self):
        """ print method """
        visited=[]
        str=''
        self._print_list(visited,self.root,str)
        #print("Content of Trie:")
        return visited
        #for i in range(len(visited)):
        #    print(visited[i])

    def _print_list(self,visited,node,str):
        index=0
        while index<26:
            if node.children[index]:
                str+=chr(ord('a')+index)
                #print(2,str)
                if node.children[index].isEndOfWord == False:
                    self._print_list(visited,node.children[index],str)
                    str=str[0 : (len(str)-1)]
                else:
                    if str not in visited:
                        visited.append(str)
                    if self.has_child(node.children[index]):
                        self._print_list(visited,node.children[index],str)
                        str=str[0 : (len(str)-1)]
            index+=1

 
if __name__ == "__main__":
    lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
    tr=Trie()
    tr.insert_from_list(lista)
    filename='../tiny_dictionary.txt'
    list_=tr.read_from_file(filename)
    tr.insert_from_list(list_)
    #print(list_)
    #print(tr.search("romino"))
    print(tr.word_count(tr.root))