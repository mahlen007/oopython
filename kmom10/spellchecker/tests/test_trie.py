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
        filename="tiny_frequency.txt"
        tr.create_from_file(filename)
        #lista=tr.read_from_file("tiny_frequency.txt")
        #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        #tr.insert_from_list(lista)
        self.assertEqual(tr.search("offer"), True, "Should be True") # Assert

    def test_search_with_right_word_but_upper_letters_ok(self):
        """ Test if search works with right word but upper letters """
        tr=Trie()
        filename="tiny_frequency.txt"
        tr.create_from_file(filename)

        #lista=tr.read_from_file("tiny_frequency.txt")
        #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        #tr.insert_from_list(lista)
        self.assertEqual(tr.search("HUMOR"), True, "Should be True") # Assert


    def test_seach_with_wrong_word_and_get_exception_ok(self):
        """ Test if exception for search works """
        tr=Trie()
        #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        filename="tiny_frequency.txt"
        tr.create_from_file(filename)
        
        #lista=tr.read_from_file("tiny_frequency.txt")
        #tr.insert_from_list(lista)
        with self.assertRaises(SearchMiss):# Assert
            tr.search("hidden")

    def test_delete_and_search_and_get_exception_ok(self):
        """ Test if delete and exception for search works """
        tr=Trie()
        filename="tiny_frequency.txt"
        tr.create_from_file(filename)

        #lista=tr.read_from_file("tiny_frequency.txt")
        #tr.insert_from_list(lista)
        tr.delete('humor')
        print(tr.search('humor'))
        with self.assertRaises(SearchMiss):# Assert
            tr.search('humor')

    def test_prefix_search_with_right_word_ok(self):
        """ Test if prefix works with right word """
        tr=Trie()
        #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        filename="tiny_frequency.txt"
        tr.create_from_file(filename)

        #lista=tr.read_from_file("tiny_frequency.txt")
        #tr.insert_from_list(lista)
        self.assertEqual(tr.prefix_search("vill"), [('villain', 10551.3)], "Should be True")
