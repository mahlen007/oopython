"""
Class for testing the Hand class
"""
import unittest
import random

from src.hand import Hand

class TestHand(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        random.seed("hand")

    def test_create_hand_ok(self):
        """ Test that instance is Hand """
        hand1=Hand() # Arrange
        self.assertIsInstance(hand1, Hand, "Instance should be Hand") # Assert

    def test_create_hand_with_list_ok(self):
        """ Test that instance is Hand """
        hand1=Hand([1,2,3,4,5]) # Arrange
        self.assertIsInstance(hand1, Hand, "Instance should be Hand") # Assert

    def test_hand_method_to_list_ok(self):
        """ Test that instance is Hand """
        list1=Hand([1,2,3,4,5]) # Arrange
        self.assertEqual(list1.to_list(), [1,2,3,4,5], "It should be the same list.") # Assert

    def test_random_hand_ok(self):
        """ Test random hand is ok """
        hand1=Hand()
        hand2=Hand([3,1,6,3,1])
        self.assertNotEqual(hand1,hand2,"The hands are the same.")

    def test_change_right_dize_ok(self):
        """ Test change right dize in hand is ok """
        hand1=Hand()  #[5,1,2,3,1]
        hand1.roll([2]) #[5,1,4,3,1]
        self.assertEqual(hand1.to_list(),[5,1,4,3,1])

    def test_change_all_dize_ok(self):
        """ Test change all dize in hand is ok """
        hand1=Hand()  #[5,1,2,3,1]
        hand1.roll() #[4,6,4,6,4]
        self.assertEqual(hand1.to_list(),[4,6,4,6,4])

    def test_hand_to_list_ok(self):
        """ Test method to_list is ok """
        hand1=Hand()  #[5,1,2,3,1]
        self.assertEqual(hand1.to_list(),[5,1,2,3,1])
