"""
Module Node
"""

class Node:
    """ Class Node """
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def is_root(self):
        """ Check if node is root """
        return self.parent is None

    def has_left_child(self):
        """ Check if node have left child """
        return self.left is not None

    def has_right_child(self):
        """ Check if node have right child """
        return self.right is not None

    def has_both_children(self):
        """ Check if node have both children """
        return self.left is not None and self.right is not None

    def has_parent(self):
        """ Check if node have parent """
        return self.parent is not None

    def is_left_child(self):
        """ Check if node is left child """
        if self.key < self.parent.key:
            return True
        return False

    def is_right_child(self):
        """ Check if node is right child """
        if self.key > self.parent.key:
            return True
        return False

    def is_leaf(self):
        """ Check if node is a leaf """
        return self.left is None and self.right is None

    def __lt__(self, other):
        """ Compare 2 keys """
        return self.key<other.key

    def __gt__(self, other):
        """ Compare 2 keys """
        return self.key>other.key

    def __eq__(self, other):
        """ Check if keys are equal """
        return self.key == other.key
