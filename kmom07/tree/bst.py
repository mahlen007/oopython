"""
Module BinarySearchTree
"""

from node import Node
import treevizer


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
        #if node is None:
        #    return None 
        node,deleted_value= self._remove(node, key)
        #print(node.key)
        #print(deleted_value)
        #if node is not None and node.parent is None:
        #    self.root = node
        return deleted_value

    @classmethod
    def _remove(cls, node, key):
        #print("*")
        if node is None:
            return None, None
        #Är ett löv
        elif node.right is None and node.left is None:
            if node.is_right_child():
                #print("Här")
                node.parent.right=None
            else:
                node.parent.left=None
            return node, node.value
        #Har ett barn
        elif node.left is None:
            if node.is_right_child():
                node.parent.right = node.right
                node.right.parent=node.parent
            else:
                node.parent.left = node.right
                node.right.parent=node.parent
            return node.right, node.value
        elif node.right is None:
            if node.is_right_child():
                node.parent.right = node.left
                node.left.parent=node.parent
            else:
                node.parent.left = node.left
                node.left.parent=node.parent
            return node.left, node.value        
        #Har 2 barn
        else:
            deleted_value=node.value
            #if node.left is None:
            #    return node.right, deleted_value
            #if node.right is None:
            #    return node.left, deleted_value
            succ = cls._find_succ(cls,node.right)
            print("Successor: "+str(succ.key))
            node.key, node.value=succ.key, succ.value
            succ.parent.left=succ.right
            #succ.right.parent=succ.parent
           
            if succ.parent is not None:
                succ.parent.left=succ.right
            else:
                succ.parent.right=succ.right
            #if node.parent is None:
            #    succ.parent is None
            #node.key=succ.key
            #node=succ
            #succ.parent.left=succ.right
            #deleted_value=node.value
            
            #node.right, _=cls._remove(node.right, succ.key)
            del succ
            #succ.parent = node.parent
        return node, deleted_value

        """
        elif key<node.parent.key and not node.has_both_children:
            #node.left, deleted_value=cls._remove(node.left, key)
            if node.left is not None:
                node.parent.left=node.left
            else:
                node.parent.left=node.right
            return node, node.value
        elif key>node.parent.key and not node.has_both_children :
            #node.right, deleted_value=cls._remove(node.right, key)
            if node.left is not None:
                node.parent.right=node.left
            else:
                node.parent.right=node.right
            return node, node.value
        """



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
    bst.insert(8, "8")
    bst.insert(5, "5")
    bst.insert(2, "2")
    bst.insert(15, "15")
    #bst.insert(4, "4")
    bst.insert(11, "11")
    bst.insert(12, "12")
    bst.insert(10, "10")
    bst.insert(0, "0")
    bst.insert(1, "1")
    bst.insert(14, "14")
    bst.insert(16, "16")
    bst.insert(7, "7")
    bst.insert(8, "8")
    bst.insert(6, "6")
    #bst.inorder_traversal_print()
    #treevizer.to_png(bst.root)
    #print(bst.remove(5))
    print(bst.remove(8))
    #bst.inorder_traversal_print()
    treevizer.to_png(bst.root, png_path="tree2.png")
