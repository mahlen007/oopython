"""
Class for testing the Scoreboard class
"""
import unittest
import random

from src.scoreboard import Scoreboard
from src.hand import Hand

class TestScoreboard(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        random.seed("hand")
        self.empty_dict = {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Three Of A Kind": -1,
            "Four Of A Kind": -1,
            "Full House": -1,
            "Small Straight": -1,
            "Large Straight": -1,
            "Yahtzee": -1,
            "Chance": -1,
        }

    def test_add_points_ok(self):
        """ Test that add_points works """
        sb=Scoreboard.from_dict(self.empty_dict) # Arrange
        hand1=Hand()
        sb.add_points("Four Of A Kind",hand1)
        self.assertEqual(sb.get_total_points(), 0, "Total score should be 1") # Assert
