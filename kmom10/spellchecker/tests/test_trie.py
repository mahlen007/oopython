"""
Class for testing the Trie class
"""
import unittest

from src.trie import Trie
from src.errors import SearchMiss

class TestUnorderlist(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        pass

    def test_search_with_right_word_ok(self):
        """ Test if search works with right word """
        tr=Trie()
        lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        tr.insert_from_list(lista)
        self.assertEqual(tr.search("horse"), True, "Should be True") # Assert

    def test_search_with_right_word_but_upper_letters_ok(self):
        """ Test if search works with right word but upper letters """
        tr=Trie()
        lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        tr.insert_from_list(lista)
        self.assertEqual(tr.search("NAME"), True, "Should be True") # Assert


    def test_seach_with_wrong_word_and_get_exception_ok(self):
        """ Test if exception for search works """
        tr=Trie()
        lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        tr.insert_from_list(lista)
        with self.assertRaises(SearchMiss):# Assert
            tr.search("hidden")
