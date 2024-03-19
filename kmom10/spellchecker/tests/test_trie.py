"""
Class for testing the Trie class
"""
import unittest

from src.trie import Trie
from src.errors import SearchMiss

class TestTrie(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        pass

    def test_search_with_right_word_ok(self):
        """ Test if search works with right word """
        #tr=Trie()
        #filename="tiny_frequency.txt"
        tr=Trie.create_from_file()
        #lista=tr.read_from_file("tiny_frequency.txt")
        #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
        #tr.insert_from_list(lista)
        self.assertEqual(tr.search("most"), True, "Should be True") # Assert

    def test_search_with_right_word_but_upper_letters_ok(self):
        """ Test if search works with right word but upper letters """
        tr=Trie.create_from_file()
        self.assertEqual(tr.search("MOST"), True, "Should be True") # Assert


    def test_seach_with_wrong_word_and_get_exception_ok(self):
        """ Test if exception for search works """
        tr=Trie.create_from_file()
        with self.assertRaises(SearchMiss):# Assert
            tr.search("bigger")

    def test_prefix_with_right_word_ok(self):
        """ Test prefix with right word """
        tr=Trie.create_from_file()
        self.assertEqual(tr.prefix_search("mostl"), [('mostly', 22658.0)], "Should be True")

    # def test_create_from_file_ok(self):
    #     """ Test create from file """
    #     tr=Trie.create_from_file()
    #     self.assertEqual(tr.word_count(self),25800, "Should be True") # Assert



    # def test_delete_and_search_and_get_exception_ok(self):
    #     """ Test if delete and exception for search works """
    #     tr=Trie.create_from_file()
    #     tr.delete('humor')
    #     print(tr.search('humor'))
    #     with self.assertRaises(SearchMiss):# Assert
    #         tr.search('humor')

    # def test_prefix_search_with_right_word_ok(self):
    #     """ Test if prefix works with right word """
    #     tr=Trie()
    #     #lista=['hoe','house','horse','name','man','hot','apply','riddle','banana','home']
    #     filename="tiny_frequency.txt"
    #     tr.create_from_file(filename)

    #     #lista=tr.read_from_file("tiny_frequency.txt")
    #     #tr.insert_from_list(lista)
    #     self.assertEqual(tr.prefix_search("vill"), [('villain', 10551.3)], "Should be True")
