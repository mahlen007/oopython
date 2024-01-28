#!/usr/bin/env python3
"""
Class for Die
"""
import random

class Die():
    """
    Die class
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value=None):
        """
        init method
        """
        if value is None:
            value=random.randint(1,6)
        elif value<Die.MIN_ROLL_VALUE:
            value=Die.MIN_ROLL_VALUE
        elif value>Die.MAX_ROLL_VALUE:
            value=Die.MAX_ROLL_VALUE
        self._value=value

    def get_name(self):
        """
        get name method
        """
        argument=self._value
        switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six"
        }
        return switcher.get(argument, "nothing")

    def get_value(self):
        """
        get value method
        """
        return self._value

    def roll(self):
        """
        roll dice method
        """
        side=random.randint(Die.MIN_ROLL_VALUE,Die.MAX_ROLL_VALUE)
        self._value=side
        return side

    def __eq__(self, other):
        """
        compare two objects or number
        """
        if self._value == other._value:
            return True
        else:
            return False


    def __str__(self):
        """
        make string method
        """
        return str(self._value)
