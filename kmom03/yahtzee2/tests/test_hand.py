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
