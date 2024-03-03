"""
Class for testing the Unorderedlist class
"""
import unittest

from src.unorderedlist import UnorderedList
from src.errors import MissingIndex
from src.errors import MissingValue

class TestUnorderlist(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        pass

    def test_get_with_right_index_ok(self):
        """ Test if get works with right index """
        ul=UnorderedList()
        ul.append("Hej")
        ul.append("Då")
        self.assertEqual(ul.get(1), "Då", "Should be Då") # Assert

    def test_get_with_wrong_index_and_get_exception_ok(self):
        """ Test if get works with right index """
        ul=UnorderedList()
        ul.append("Hej")
        ul.append("Då")
        with self.assertRaises(MissingIndex):# Assert
            ul.get(2)

    def test_remove_with_wrong_index_and_get_exception_ok(self):
        """ Test if get works with right index """
        ul=UnorderedList()
        ul.append("Hej")
        ul.append("Då")
        with self.assertRaises(MissingValue):# Assert
            ul.remove("Igen")

    def test_remove_with_right_index_ok(self):
        """ Test if get works with right index """
        ul=UnorderedList()
        ul.append("Hej")
        ul.append("Då")
        ul.remove("Då")
        self.assertEqual(ul.size(), 1, "Should be 1") # Assert
