#!/usr/bin/env python3
"""
Class for Node in trie
"""
class Node:
    """ Class Node """
    def __init__(self,char='&',freq=1):
        self.children=[None]*26#[None for _ in range(26)]
        self.data=char
        self.isEndOfWord=False
        self.freq=freq

if __name__ == "__main__":
    pass
