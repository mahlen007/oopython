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
        if node.is_root() and node.is_leaf():
            deleted_value=node.value
            self.root=None
        elif node.is_root() and node.right is None:
            self.root=node.left
            node.left.parent=None
        node,deleted_value= self._remove(node)
        return deleted_value

    @classmethod
    def _remove(cls, node):
        """ Inner Remove method """
        if node is None:
            return None, None
        #Is a leaf
        if node.is_leaf() and node.parent is None:
            deleted_value=node.value
            node.value=None
            cls.root=None
            node.parent=None
            return None, deleted_value
        if node.is_leaf():
            if node.is_right_child():
                node.parent.right=None
            else:
                node.parent.left=None
            node.parent=None
            return node, node.value
        #Have one child
        if node.left is None or node.right is None:
            return cls._check_one_child(node)
        #Have 2 children
        return cls._check_two_children(node)

    @classmethod
    def _check_one_child(cls,node):
        """ Check one child """
        if node.left is None:
            if node.is_left_child():
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            if node.right:
                node.right.parent=node.parent
            node.parent=None
            return node, node.value
        if node.right is None and node.parent is not None:
            if node.is_right_child():
                node.parent.right = node.left
            else:
                node.parent.left = node.left
            if node.left:
                node.left.parent = node.parent
            node.parent=None
            return node, node.value
        if node.right is None and node.parent is None:
            deleted_value=node.value
            cls.root=node.left
            node=node.left
        return node, deleted_value

    @classmethod
    def _check_two_children(cls,node):
        """ Check two children """
        deleted_value=node.value
        succ = cls._find_succ(cls,node.right)
        node.key, node.value=succ.key, succ.value
        if succ.parent.left is not None and succ.parent is not node:
            succ.parent.left=succ.right
        elif succ.parent is node:
            if succ.right is not None:
                succ.right.parent=node
                node.right=succ.right
        if succ.has_right_child() and succ.parent is not node:
            succ.right.parent=succ.parent
        if succ.is_leaf() and succ.parent is node:
            node.right=None
        return node, deleted_value


    def _find_succ(self, node):
        """ Find succeror"""
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
        return (cls._size(node.left)+1+cls._size(node.right))

if __name__== "__main__":
    bst = BinarySearchTree()
    """Test1"""
    bst.insert(3, "3")
    bst.insert(8, "8")
    bst.insert(5, "5")
    bst.insert(6, "6")
    bst.insert(1, "1")
    bst.insert(0, "0")
    bst.insert(2, "2")
    bst.insert(4, "4")
    bst.insert(9, "9")
    bst.insert(7, "7")
    #treevizer.to_png(bst.root)
    print(bst.remove(3))
    #treevizer.to_png(bst.root, png_path="tree1.png")
    print(bst.remove(4))
    #treevizer.to_png(bst.root, png_path="tree2.png")
    print(bst.remove(5))
    print(bst.remove(6))
    #treevizer.to_png(bst.root, png_path="tree3.png")
    print(bst.remove(7))
    #treevizer.to_png(bst.root, png_path="tree4.png")
    print(bst.remove(8))
    #treevizer.to_png(bst.root, png_path="tree5.png")
    print(bst.remove(9))
    #print(bst.inorder_traversal_print())
    #treevizer.to_png(bst.root, png_path="tree6.png")
    print(bst.remove(1))
    print(bst.remove(2))
    print(bst.remove(0))
    #treevizer.to_png(bst.root, png_path="tree7.png")
