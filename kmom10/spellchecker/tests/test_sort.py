"""
Class for testing the Unorderedlist class
"""
import unittest

from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion

class TestSort(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        pass

    def test_recursive_sort_ok(self):
        """ Test recursive sort works """
        ul=UnorderedList()
        ul.append(3)
        ul.append(4)
        ul.append(2)
        recursive_insertion(ul, ul.size())
        self.assertEqual(ul.get(0), 2, "Should be 2") # Assert

    def test_recursive_sort_without_items_ok(self):
        """ Test recursive sort works without items """
        ul = UnorderedList()
        recursive_insertion(ul,0)
        self.assertEqual(ul.size(), 0)
