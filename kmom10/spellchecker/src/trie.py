#!/usr/bin/env python3
"""
Class for Trie
"""
from src.node import Node
from src.errors import SearchMiss
#from src.errors import MissingValue

class Trie():
    """ Class Trie """
    def __init__(self):
        self.root=Node()

    def getNode():
        pNode = TrieNode()
        pNode.isEndOfWord = False
        return pNode

    def has_child(self,node):
        for i in range(26):
            if node.children[i]:
                return True
        return False

    def add_word(self, word):
        """ Insert a word in the trie """
        current = self.root
        for letter in word:
            #current.data=letter
            index=ord(letter)-ord('a')
            if not current.children[index]:
                current.children[index]=Node(letter)
                current.data=letter
            current=current.children[index]
        current.isEndOfWord=True

    def search(self, word):
        """ Search for a word in the trie """
        word=word.lower()
        current=self.root

        for letter in word:
            index=ord(letter)-ord('a')
            if not current.children[index]:
                raise SearchMiss
            current=current.children[index]
        return current.isEndOfWord==True


    def isEmpty(self,node):
        for i in range(26):
            if node.children[i]:
                return False
        return True

    def insert_from_list(self,list_word):
        """ read from a list and insert """
        for word in list_word:
            self.add_word(word)

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
                    str=str[: -1]
                else:
                    if str not in visited:
                        visited.append(str)
                    if self.has_child(node.children[index]):
                        self._print_list(visited,node.children[index],str)
                        str=str[:-1]
            index+=1

    def prefix_search(self,prefix):
        """ print method """
        prefix=prefix.lower()
        visited=[]
        str=''
        node=self.root
        for letter in prefix:
            if node.children[ord(letter)-ord('a')] is None:
                raise SearchMiss
            node=node.children[ord(letter)-ord('a')] 
        visited=self._prefix_search(visited,node,str,prefix)
        #print("Content of Trie:")
        return visited
        #for i in range(len(visited)):
        #    print(visited[i])

    def _prefix_search(self,visited,node,str,prefix):
        index=0
        while index<26:
            if node.children[index]:
                str+=chr(ord('a')+index)
                #print(2,str)
                if node.children[index].isEndOfWord == False:
                    self._prefix_search(visited,node.children[index],str,prefix)
                    str=str[: -1]
                else:
                    if str not in visited:
                        visited.append(prefix+str)
                    if self.has_child(node.children[index]):
                        self._prefix_search(visited,node.children[index],str,prefix)
                        str=str[:-1]
            index+=1
        return visited





    def __contains__():
        pass

    def __getitem__():
        pass

    def __setitem__():
        pass

    def __str__():
        pass

    def __iter__():
        pass

    def __delitem__():
        pass

    def delete(self, word):
        word=word.lower()
        return self.deleteHelper(self.root, word, 0)

    def deleteHelper(self, curr, word, index):
        if index == len(word):
            
            if not curr.isEndOfWord:
                return False
            curr.isEndOfWord = False
            return len(curr.children) == 0
        ch = word[index]
        if curr.children[ord(ch)-ord('a')] == None:
            return False
        child = curr.children[ord(ch)-ord('a')]
        shouldDeleteChild = self.deleteHelper(child, word, index + 1)
        if shouldDeleteChild:
            del curr.children[ord(ch)-ord('a')]
            return len(curr.children) == 0
        return False



 
if __name__ == "__main__":
    lista=['hood','house','horse','name','man','hit','apply','riddle','banana','home','mandoline','make','map']
    tr=Trie()
    #root = getNode()
    tr.insert_from_list(lista)
    filename='../tiny_dictionary.txt'
    #list_=tr.read_from_file(filename)
    #tr.insert_from_list(list_)
    #print(tr.print_list())
    #print(tr.search("romano"))
    #print(tr.delete("man"))
    #print(tr.search("romano"))
    print(tr.print_list())
    #print(tr.starts_with('ma'))
    #print(tr.autocomplete('ma'))
    print(tr.prefix_search('H'))
    #print(tr.word_count(tr.root))