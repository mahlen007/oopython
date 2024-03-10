"""
Class for testing the Die class
"""
import unittest
import random

from src.die import Die

class TestDie(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        random.seed("die")

    def test_create_die_ok(self):
        """ Test that instance is Die """
        die=Die() # Arrange
        self.assertIsInstance(die, Die, "Instance should be Die") # Assert

    def test_create_die_with_right_value_ok(self):
        """ Test create die with right value """
        die=Die(1) # Arrange
        self.assertEqual(die.get_value(), 1, "Create die with right value")# Assert

    def test_create_die_with_wrong_value_ok(self):
        """ Test create die with wrong value """
        die=Die(100) # Arrange
        self.assertEqual(die.get_value(), 6, "Create die with wrong value. Change to 6.")# Assert

    def test_roll_get_new_value_ok(self):
        """ Test die roll """
        die=Die() # Arrange
        self.assertEqual(die.roll(), 5, "Test to roll die.")# Assert

    def test_get_name_ok(self):
        """ Test die get name """
        die=Die(4) # Arrange
        self.assertEqual(die.get_name(), 'four', "Test right name with letters.")# Assert

    def test_equal_ok(self):
        """ Test die equal """
        die1=Die(4) # Arrange
        die2=Die(4)
        self.assertEqual(die1, die2, "They are the same")# Assert

    def test_not_equal_ok(self):
        """ Test die equal """
        die1=Die(3) # Arrange
        die2=Die(4)
        self.assertNotEqual(die1,die2, "They are the not same")# Assert
