class Node:
    """ Class Node """
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def has_next(self):
        return self.next is not None

class UnorderedList():
    """ Class Unordered List """
    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, value):
        """ append """
        tmp = Node(value)
        if self._head is None:
            self._head = tmp
        else:
            current = self._head
            while current.has_next():
                current = current.next
            current.next = tmp

    def print_list(self):
        current = self._head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    ul = UnorderedList()
    ul.append(10)
    ul.append("hej")
    ul.append(1)
    #treevizer.to_png(ul._head, "ll")
    ul.append(3)
    ul.print_list()

