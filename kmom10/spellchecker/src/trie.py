#!/usr/bin/env python3
"""
Class for Trie
"""
#import re
from src.node import Node
from src.errors import SearchMiss
#from src.errors import MissingValue

class Trie():
    """ Class Trie """
    def __init__(self):
        self.root=Node()

    #def getNode():
    #    """ print method """
    #    pNode = TrieNode()
    #    pNode.is_end_of_word = False
    #    return pNode

    def has_child(self,node):
        """ has children """
        for i in range(26):
            if node.children[i]:
                return True
        return False

    def add_word(self, line):
        """ Insert a word in the trie """
        current = self.root
        word=line.split(" ")[0]
        freq=line.split(" ")[-1]
        freq=float(freq)
        for letter in word:
            index=ord(letter)-ord('a')
            if not current.children[index]:
                current.children[index]=Node(letter)
                #current.data=letter
            current=current.children[index]
            current.data=letter
        current.freq=freq
        current.is_end_of_word=True

    def search(self, word):
        """ Search for a word in the trie """
        word=word.lower()
        current=self.root

        for letter in word:
            index=ord(letter)-ord('a')
            if not current.children[index]:
                raise SearchMiss
            current=current.children[index]
        return current.is_end_of_word is True


    def is_empty(self,node):
        """ is children empty """
        for i in range(26):
            if node.children[i]:
                return False
        return True

    def insert_from_list(self,list_word):
        """ read from a list and insert """
        for word in list_word:
            self.add_word(word)

    def read_from_file(self,fname):
        """ read from file """
        list_=[]
        with open(fname, 'r', encoding='utf-8') as openfile:
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
        if node.is_end_of_word is True:
            result += 1
        for x in range(26):
            if node.children[x] is not None:
                result += self.word_count(node.children[x])
        return result

    def print_list(self):
        """ print method """
        visited=[]
        str_=''
        self._print_list(visited,self.root,str_)
        #print("Content of Trie:")
        return visited
        #for i in range(len(visited)):
        #    print(visited[i])

    def _print_list(self,visited,node,str_):
        """ print method """
        index=0
        while index<26:
            if node.children[index]:
                #str+=chr(ord('a')+index)
                str_+=node.children[index].data
                #print(2,str)
                if node.children[index].is_end_of_word is False:
                    self._print_list(visited,node.children[index],str_)
                    str_=str_[:-1]
                else:
                    if str_ not in visited:
                        visited.append(str_)
                    if self.has_child(node.children[index]):
                        self._print_list(visited,node.children[index],str_)
                        str_=str_[:-1]
            index+=1

    def prefix_search(self,prefix):
        """ prefix search """
        prefix=prefix.lower()
        visited=[]
        str_=''
        node=self.root
        for letter in prefix:
            if node.children[ord(letter)-ord('a')] is None:
                return []
            node=node.children[ord(letter)-ord('a')]
        visited=self._prefix_search(visited,node,str_,prefix)
        #print("Content of Trie:")
        pr_sort=[]
        prefix_sorted=self.sort_prefix(visited)
        if self.search(prefix):
            visited.append((prefix,node.freq))
        if len(prefix_sorted)<=10:
            return prefix_sorted
        for x in range(10):
            pr_sort.append(prefix_sorted[x])
        return pr_sort

        #for i in range(len(visited)):
        #    print(visited[i])

    def _prefix_search(self,visited,node,str_,prefix):
        """ prefix search """
        index=0
        while index<26:
            if node.children[index]:
                str_+=node.children[index].data
                #str+=chr(ord('a')+index)
                #print(2,str)
                if node.children[index].is_end_of_word is False:
                    self._prefix_search(visited,node.children[index],str_,prefix)
                    str_=str_[:-1]
                else:
                    if str_ not in visited:
                        #print(node.children[index].freq)
                        visited.append((prefix+str_,node.children[index].freq))
                    if self.has_child(node.children[index]):
                        self._prefix_search(visited,node.children[index],str_,prefix)
                        str_=str_[:-1]
            index+=1
        return visited

    def sort_prefix(self,my_list):
        """ sort prefix list """
        length = len(my_list)
        for i in range(0, length):
            for j in range(0, length-i-1):
                if my_list[j][1] < my_list[j + 1][1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
        return my_list

    def correct_spelling(self,word):
        """ check spelling """
        word=word.lower()
        node=self.root
        one_right=True
        try:
            if self.search(word):
                return word
        except SearchMiss:
            pass
        for letter in word:
            if node.children[ord(letter)-ord('a')] is None:
                return []
            if letter==node.children[ord(letter)-ord('a')]:
                one_right=True
        visited=self._prefix_search(visited,node,str_,prefix)

    def _correct_spelling(self,visited,node,str_,prefix):
        """ check spelling """
        index=0
        while index<26:
            if node.children[index]:
                str_+=node.children[index].data
                #str+=chr(ord('a')+index)
                #print(2,str)
                if node.children[index].is_end_of_word == False:
                    self._prefix_search(visited,node.children[index],str_,prefix)
                    str_=str_[:-1]
                else:
                    if str_ not in visited:
                        #print(node.children[index].freq)
                        visited.append((prefix+str_,node.children[index].freq))
                    if self.has_child(node.children[index]):
                        self._prefix_search(visited,node.children[index],str_,prefix)
                        str_=str_[:-1]
            index+=1
        return visited

    def delete(self, word):
        """ delete word """
        #word=word[0]
        word=word.lower()
        #print(word)
        return self._delete(self.root, word, 0)

    def _delete(self, curr, word, index):
        """ delete word """
        if index == len(word):
            if not curr.is_end_of_word:
                return False
            curr.is_end_of_word = False
            return len(curr.children) == 0
        ch = word[index]
        if curr.children[ord(ch)-ord('a')] is None:
            return False
        child = curr.children[ord(ch)-ord('a')]
        should_delete_child = self._delete(child, word, index + 1)
        if should_delete_child:
            del curr.children[ord(ch)-ord('a')]
            return len(curr.children) == 0
        return False

if __name__ == "__main__":
    tr=Trie()
    #root = getNode()
    #tr.insert_from_list(lista)
    filename='../tiny_frequency.txt'
    lista=tr.read_from_file(filename)
    tr.insert_from_list(lista)
    #print(tr.print_list())
    print(tr.search("romano"))
    print(tr.delete("humor"))
    print(tr.delete("humor"))
    print(tr.print_list())
    #print(tr.starts_with('ma'))
    #print(tr.autocomplete('ma'))
    #print(tr.prefix_search('H'))
    #print(tr.word_count(tr.root))
