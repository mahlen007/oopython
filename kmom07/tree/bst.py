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
        node,deleted_value= self._remove(node, key)
        return deleted_value

    @classmethod
    def _remove(cls, node, key):
        if node is None:
            return None, None
        #Är ett löv
        elif node.left is None and node.right is None and node.parent is None:
            deleted_value=node.value
            node.parent=None
            cls.root=None
            return cls.root, deleted_value
        elif node.is_leaf(): 
            if node.is_right_child():
                node.parent.right=None
            else:
                node.parent.left=None
            node.parent=None
            return node, node.value
        #Har ett barn
        elif node.left is None:
            if node.is_left_child():
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            if node.right:
                node.right.parent=node.parent
            node.parent=None
            return node, node.value 
        elif node.right is None and node.parent is not None:
            print("problem"+str(node.key))
            if node.is_right_child():
                node.parent.right = node.left
            else:
                node.parent.left = node.left
            if node.left: 
                node.left.parent = node.parent          
            node.parent=None
            return node, node.value
        elif node.right is None and node.parent is None:
            #treevizer.to_png(bst.root, png_path="tree5.png")
            deleted_value=node.value
            #succ=node.left
            #node.key, node.value=succ.key, succ.value
            #node.left=succ.left
            #node.right=succ.right 
            #cls.root=node
            node.left.parent=None
            node.parent=None
            #node.left.parent=None
            return node, deleted_value
        #Har 2 barn
        else:
            deleted_value=node.value
            succ = cls._find_succ(cls,node.right)
            print("Node: "+str(node.key)+"succ: "+str(succ.key))
            node.key, node.value=succ.key, succ.value
            if succ.parent.left is not None and succ.parent is not node:
                succ.parent.left=succ.right
            elif succ.parent is node:
                
                #node.parent=None
                if succ.right is not None:
                    
                    succ.right.parent=node
                    node.right=succ.right
            if succ.has_right_child() and succ.parent is not node:
                succ.right.parent=succ.parent
            if succ.is_leaf() and succ.parent is node:
                print("test")
                node.right=None
            print("2.Node: "+str(node.key)+"succ: "+str(succ.key))
            #if succ.parent.left is not None:
            #    succ.parent.left=None
            #else:
            #    succ.parent.right=None
            #node.right, _ = cls._remove(node.right, succ.key)
            if node.right is None:
                cls.root=node
                #node.parent=cls.root
        return node, deleted_value


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
    treevizer.to_png(bst.root)
    print(bst.remove(3))
    treevizer.to_png(bst.root, png_path="tree1.png")
    print(bst.remove(4))
    treevizer.to_png(bst.root, png_path="tree2.png")
    print(bst.remove(5))
    print(bst.remove(6))
    treevizer.to_png(bst.root, png_path="tree3.png")
    print(bst.remove(7))
    treevizer.to_png(bst.root, png_path="tree4.png")
    print(bst.remove(8))
    treevizer.to_png(bst.root, png_path="tree5.png")
    print(bst.remove(9))
    
    print(bst.remove(1))
    print(bst.remove(2))
    print(bst.remove(0))
    treevizer.to_png(bst.root, png_path="tree6.png")
    """
    bst.insert(9, "9")
    bst.insert(5, "5")
    bst.insert(2, "2")
    bst.insert(15, "15")
    bst.insert(4, "4")
    bst.insert(3, "3")
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

    treevizer.to_png(bst.root,png_path="tree1b.png")
    print(bst.remove(5))
    print(bst.remove(0))
    treevizer.to_png(bst.root,png_path="tree2b.png")
    print(bst.remove(2))
    treevizer.to_png(bst.root,png_path="tree3b.png")
    print(bst.remove(3))
    treevizer.to_png(bst.root,png_path="tree4b.png")
    print(bst.remove(14))
    print(bst.remove(16))
    print(bst.remove(4))
    print(bst.remove(15))
    print(bst.remove(1))
    """
