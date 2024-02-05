from src.hand import Hand
from src.rules import Chance, Yahtzee, FullHouse

class Scoreboard:
    """ Scoreboard class """
    points = {
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


    def __init__(self,name):
        self._total_points=0

    def get_total_points(self):
        """ Get total points """
        pos_sum = sum(value for value in points.values() if isinstance(value, (int)) and value > 0)
        return pos_sum
        # point=0
        # for value in points.values():
        #     print ("** "+value)
        #     if value!=-1:
        #         point+=value
        # return point

    def add_points(self, cls, rule_name, hand):
        """ Add points """
        #hand1=hand
        self.points[rule_name]=cls(rule_name).get_points(hand)

    def get_points(self, rule_name):
        """ Get points """
        print(rule_name)
        return self.points[rule_name]

    def finished():
        """ Check if finished """
        if -1 in self.points.values():
            return False
        return True

    @classmethod
    def from_dict(cls,points=None):
        """ Get from dict """
        sb=cls(points)
        #for index, value in points:
        #    sb = cls(index, value)
        return sb
