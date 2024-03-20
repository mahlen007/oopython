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
        tr=Trie.create_from_file()
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

    def test_prefix_with_right_amount_of_answers_ok(self):
        """ Test prefix with right amount of answers """
        tr=Trie.create_from_file()
        self.assertEqual(len(tr.prefix_search("the")), 10, "Should be True")

    def test_delete_and_search_and_get_exception_ok(self):
        """ Test if delete and exception for search works """
        tr=Trie.create_from_file()
        tr.delete('biggest')
        with self.assertRaises(SearchMiss):# Assert
            tr.search('biggest')

    def test_print_all_word_and_count_ok(self):
        """ Test print all words and count the words """
        tr=Trie.create_from_file()
        self.assertEqual(len(tr.print_list()),25402, "Should be 25402") # Assert
