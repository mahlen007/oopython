#!/usr/bin/env python3
"""
Class for Node in trie
"""
class Node:
    """ Class Node """
    def __init__(self):
        self.children=[None]*26#[None for _ in range(26)]
        self.isEndOfWord=False

if __name__ == "__main__":
    pass
