#!/usr/bin/env python3
"""
Class for Hand with dice
"""
from src.die import Die

class Hand():
    """
    Hand class
    """

    def __init__(self,dice_values=None):
        """
        init method
        """
        self.dice=[]
        if dice_values is None:
            for x in range(5):
                self.dice.append(Die())
        else:
            for x in range(5):
                self.dice.append(Die(dice_values[x]))


    def roll(self,my_list=None):
        """
        roll the dice method
        """
        if my_list is None:
            my_list=[0,1,2,3,4]
        for x in range(5):
            if x in my_list:
                self.dice[x]= Die()

    def to_list(self):
        """ Put the numbers in a list """
        my_list=[]
        for number in self.dice:
            my_list.append(number.get_value())
        return my_list

    def __str__(self):
        """
        make a string method
        """
        strang=""
        for x in range(5):
            die=self.dice[x]
            strang+=str(die)+", "
        return strang[:len(strang)-2]

    def dice_name(self):
        """
        get dice name method
        """
        strang=""
        for x in range(5):
            die=self.dice[x]
            strang+=str(die.get_name())+", "
        return strang[:len(strang)-2]
