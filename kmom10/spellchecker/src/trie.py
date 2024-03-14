#!/usr/bin/env python3
"""
Class for Trie
"""
from node import Node
from errors import SearchMiss
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
            index=ord(letter)-ord('a')
            if not current.children[index]:
                current.children[index]=Node()
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

    def prefix_search(self, prefix):
        prefix=prefix.lower()
        result=[]
        current=self.root
        for letter in prefix:
            index=ord(letter)-ord('a')
            if current.children[index] is None: 
                return result
            current=current.children[index]
        traverse(current, result, prefix)
        return result

    def traverse(self, node,leaves, parent):
        if node.children is None:
            leaves.add(parent)
            return leaves
        for i in range(node.children.length):
            if (node.children[i] is not None):
                letter=chr(i)
                traverse(node.children[i], leaves, parent+letter)
        return leaves

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
                    str=str[0 : (len(str)-1)]
                else:
                    if str not in visited:
                        visited.append(str)
                    if self.has_child(node.children[index]):
                        self._print_list(visited,node.children[index],str)
                        str=str[0 : (len(str)-1)]
            index+=1

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

    def starts_with(self, prefix):
        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        '''
        words = []
        current = self.root
        for char in prefix:
            if current.children[ord(char)-ord('a')] is None:
            #if char not in current.children:
                # Could also just return words since it's empty by default
                raise SearchMiss #return words
            current=current.children[ord(char)-ord('a')]
            #current = current.children[char]
        word=prefix
        # Step 2
        words=self._child_words_for(current, word,words)
        return words

    @classmethod
    def _child_words_for(cls, node,word, words,length=0):
        count=0
        if node.isEndOfWord:
        #if node.is_word:
            words.append(word)
            word=word[:length-1-count]
        for i in range(26):
        #for letter in node.children:
            if node.children[i]:
                letter=chr(i+ord('a'))
                count+=1
                length=len(word)
                word=word+letter
                
                words=cls._child_words_for(node.children[ord(letter)-ord('a')],word, words,length)
                if node.isEndOfWord:
                    words.append(word)
                    print(word)
                    word=word[:len(word)-1-count]
                    print('*'+word)
        return words
        

    def get_word_beginning_with(self, query): 
        
        words = [] # The answer
        slate = list(query) # temp cache to append chars to
        curr = self.root
        def movebychar(char, curr):
            # inner helper function to find subtree
            for child in curr.children:
                if child.val == char:
                    return child
            return None # Couldn't find child, return None
        def add_word_with_dfs(curr):
            # inner helper function to perform DFS and populate answer 
            if curr is None:
                return
            if curr.isword:
                words.append("".join(slate[:]))
            for child in curr.children:
                if child is not None:
                    slate.append(child.val)
                    add_word_with_dfs(child)
                    slate.pop()
        # Find subtree that begins with last query character
        for char in query:
            curr = movebychar(char, curr)
            if curr is None:  # Cant go any further
                break
        # At this point, we have found a subtree with its root node
        # value equal to last of query char.
        # Recursively traverse with DFS
        add_word_with_dfs(curr)
        # Finally, return answer
        return words



 
if __name__ == "__main__":
    lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home','mandoline','make','map']
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
    #print(tr.print_list())
    #print(tr.starts_with('ma'))
    print(tr.starts_with('ma'))
    #print(tr.word_count(tr.root))