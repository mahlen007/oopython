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
        elif node.key==key:
            return node
        elif key<node.key:
            return cls._get(node.left, key)
        elif key>node.key:
            return cls._get(node.right,key)
        else:
            raise KeyError

    def remove(self, key):
        """ Remove method """
        node = self._remove(self.root, key)
        #print(node)
        #node=self._get(self.root, key)
        #if node == None:
        #    raise KeyError("Key saknas")
        #if self.get(key)==None:
            
        #node=self._remove(node, key)
        return node.value

    @classmethod
    def _remove(cls, node, key):
        if node is None:
            return node


        if key < node.key:
            node.left = cls._remove(node.left, key)

        elif key > node.key:
            node.right = cls._remove(node.right, key)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = cls._min_node(cls,node.right).key
            node.right = cls._remove(node.right, node.key)

        return node

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current



    
    
    """
    def _remove(cls, node, key):
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left=None
                return node
            else:
                node.parent.right=None
                return node
        elif not node.has_both_children():
            if node<node.parent:
                node.parent.left=node.left
                return node
            else:
                node.parent.right=node.right
                return node
        elif node.has_both_children():
            successor_parent=node
            successor=node.right
            while successor.left is not None:
                successor_parent=successor
                successor=successor.left
            if successor_parent is not node:
                successor_parent.left=successor.right
            else:
                successor_parent.right=successor.right
            node.key = successor.key
            return node
"""
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
    bst.insert(6, "first")
    bst.insert(4, "second")
    bst.insert(3, "third")
    bst.insert(5, "fourth")
    bst.insert(11, "fifth")
    bst.insert(4, "hej")
    #bst.inorder_traversal_print()
    print(bst.remove(40))
    bst.inorder_traversal_print()

    #treevizer.to_png(bst.root)
