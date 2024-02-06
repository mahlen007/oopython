""" Rule module """
from abc import ABC, abstractmethod
#from src.hand import Hand

class Rule(ABC):
    """ Abstract Rule class"""
    list_of_value=[0,0,0,0,0,0]

    @abstractmethod
    def points(self, hand):
        """ Abstract point method """

    def count_dice(self, hand):
        """ Count the dice """
        self.list_of_value=[0,0,0,0,0,0]
        for die in hand.dice:
            self.list_of_value[die.get_value()-1]+=1

class ThreeOfAKind(Rule):
    """ Three Of A Kind class"""
    def __init__(self):
        self.name = "Three Of A Kind"

    def points(self, hand):
        """ Count the point with 3 of a kind """
        self.count_dice(hand)
        test=False
        points=0
        for x in range(6):
            points+=self.list_of_value[x]*(x+1)
            if self.list_of_value[x]>=3:
                test=True
        if test:
            return points
        return 0

class FourOfAKind(Rule):
    """ Four Of A Kind class"""
    def __init__(self):
        self.name = "Four Of A Kind"

    def points(self, hand):
        self.count_dice(hand)
        #my_list=hand.to_list().sort()
        sorted_list=sorted(hand.to_list())
        print(sorted_list)
        test=False
        point=0
        for x in range(6):
            point+=self.list_of_value[x]*(x+1)
            if self.list_of_value[x]>=4:
                test=True
        if test:
            return point
        return 0

class FullHouse(Rule):
    """ Full House class"""
    def __init__(self):
        self.name = "Full House"

    def points(self, hand):
        s_list=sorted(hand.to_list())
        if (s_list[0] == s_list[1] == s_list[2] and s_list[3] == s_list[4]) or \
            (s_list[0] == s_list[1] and s_list[2] == s_list[3] == s_list[4]):
            return 25
        return 0

        # self.count_dice(hand)
        # at_least_two=0
        # for x in range(6):
        #     if self.list_of_value[x]>=2:
        #         at_least_two += 1
        # if at_least_two ==2:
        #     return 25
        # return 0

class SmallStraight(Rule):
    """ Small Straight class"""
    def __init__(self):
        self.name = "Small Straight"

    def points(self, hand):
        # s_list=sorted(hand.to_list())
        # for i in range(len(s_list) - 3):
        #     if s_list[i] == s_list[i + 1] - 1 == s_list[i + 2] - 2 == s_list[i + 3] - 3:
        #         return 30
        # return 0
        self.count_dice(hand)
        if (self.list_of_value[0]>=1 and self.list_of_value[1]>=1 and self.list_of_value[2]>=1
             and self.list_of_value[3]>=1) or (self.list_of_value[1]>=1 and self.list_of_value[2]>=1
             and self.list_of_value[3]>=1 and self.list_of_value[4]>=1) or (self.list_of_value[2]>=1
             and self.list_of_value[3]>=1 and self.list_of_value[4]>=1 and self.list_of_value[5]>=1):
            return 30
        return 0

class LargeStraight(Rule):
    """ Large Straight class"""
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand):
        s_list=sorted(hand.to_list())
        for i in range(len(s_list) - 4):
            if s_list[i] == s_list[i + 1] - 1 == s_list[i + 2] - 2 == \
                s_list[i + 3] - 3 == s_list[i + 4] - 4:
                return 40
        return 0

class Yahtzee(Rule):
    """ Yahtzee class"""
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand):
        s_list=sorted(hand.to_list())
        if s_list[0]==s_list[4]:
            return 50
        return 0

class Chance(Rule):
    """ Chance class"""
    def __init__(self):
        self.name = "Chance"

    def points(self,hand):
        points=0
        for die in hand.dice:
            points += die.get_value()
        return points

class SameValueRule(Rule):
    """ Same Value Rule class"""
    def __init__(self, value, name):
        self.name=name
        self.value=value

    def points(self, hand):
        points=0
        for die in hand.dice:
            if die.get_value() == self.value:
                points+=die.get_value()
        return points

class Ones(SameValueRule):
    """ Ones class"""
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """ Twos class"""
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """ Threes class"""
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """ Fours class"""
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """ Fives class"""
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """ Sixes class"""
    def __init__(self):
        super().__init__(6, "Sixes")
