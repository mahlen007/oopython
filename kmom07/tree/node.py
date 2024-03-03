class Node:

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left is not None
    
    def has_right_child(self):
        return self.right is not None

    def has_both_children(self):
        return self.left is not None and self.right is not None

    def has_parent(self):
        return self.parent is not None
    
    def is_left_child(self):
        if self.key < self.parent.key:
            return True
        return False

    def is_right_child(self):
        if self.key > self.parent.key:
            return True
        return False

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.key<other.key

    def __gt__(self, other):
        return self.key>other.key

    def __eq__(self, other):
        return self.key == other.key
