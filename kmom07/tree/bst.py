"""
Module BinarySearchTree
"""

from node import Node
#import treevizer


class BinarySearchTree:
    """ Class BST """
    def __init__(self):
        self.root=None

    def insert(self, key, value):
        """ Insert method """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    @classmethod
    def _insert(cls, node, key, value):
        """ Inner insert method """
        if key < node.key:
            if node.left is not None:
                cls._insert(node.left, key, value)
            else:
                node.left = Node(key, value, node)
        elif key > node.key:
            if node.right is not None:
                cls._insert(node.right, key, value)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value

    def inorder_traversal_print(self):
        """ Print method """
        self._inorder_traversal_print(self.root)

    @classmethod
    def _inorder_traversal_print(cls, node):
        """ Inner print method """
        if node is None:
            return
        if node.has_left_child():
            cls._inorder_traversal_print(node.left)
        print(node.key)
        if node.has_right_child():
            cls._inorder_traversal_print(node.right)

    def get(self, key):
        """ Get method """
        node=self._get(self.root, key)
        return node.value

    @classmethod
    def _get(cls, node, key):
        """ Inner get method """
        if node is None:
            raise KeyError("Key saknas")
        if node.key==key:
            return node
        if key<node.key:
            return cls._get(node.left, key)
        if key>node.key:
            return cls._get(node.right,key)
        raise KeyError

    def remove(self, key):
        """ Remove method """
        node=self._get(self.root,key)

        node= self._remove(node, key)
        return node.value

    @classmethod
    def _remove(cls, node, key):
        if node is None:
            return None
        elif node.is_leaf():
            if node.is_right_child():
                node.parent.right=None
                return node
            else:
                node.parent.left=None
                return node
        elif key<node.key:
            node.left=cls._remove(node.left, key)
        elif key>node.key:
            node.right=cls._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            succ = cls._find_succ(cls,node.right)
            node.key=succ.key
            #node=succ
            succ.parent.left=succ.right
            node.right=cls._remove(node.right, succ.key)
        return node

    def _find_succ(self, node):
        while node.left is not None:
            node=node.left
        return node

    def size(self):
        """ Size method """
        return self._size(self.root)

    @classmethod
    def _size(cls, node):
        """ Inner size method """
        if node is None:
            return 0
        else:
            return (cls._size(node.left)+1+cls._size(node.right))

if __name__== "__main__":
    bst = BinarySearchTree()
    bst.insert(8, "first")
    bst.insert(5, "second")
    bst.insert(2, "third")
    bst.insert(15, "fourth1")
    bst.insert(4, "fifth")
    bst.insert(11, "hej")
    bst.insert(12, "first")
    bst.insert(10, "second")
    bst.insert(0, "third")
    bst.insert(1, "fourth2")
    bst.insert(14, "fifth")
    bst.insert(16, "hej")
    bst.insert(7, "first")
    bst.insert(8, "second")
    bst.insert(6, "third")
    #bst.inorder_traversal_print()
    #treevizer.to_png(bst.root)
    #print(bst.remove(5))
    print(bst.remove(0))
    #bst.inorder_traversal_print()
    #treevizer.to_png(bst.root)
