""" Scoreboard module """
#from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes, \
    ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight, LargeStraight, \
    Yahtzee, Chance


class Scoreboard:
    """ Scoreboard class """

    def __init__(self, points):
        self.points=points
        self._total_points=0

        """ self.points = {
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
            "Chance": -1
        } """


        # self.Ones=my_dict["Ones"]
        # self.Twos=my_dict["Twos"]
        # self.Threes=my_dict["Threes"]
        # self.Fours=my_dict["Fours"]
        # self.Fives=my_dict["Fives"]
        # self.Sixes=my_dict["Sixes"]
        # self.ThreeOfAKind=my_dict["Three Of A Kind"]
        # self.FourOfaKind=my_dict["Four Of A Kind"]
        # self.FullHouse=my_dict["Full House"]
        # self.SmallStraight=my_dict["Small Straight"]
        # self.LargeStraight=my_dict["Large Straight"]
        # self.Yahtzee=my_dict["Yahtzee"]
        # self.Chance=my_dict["Chance"]
        self.dict_class = {
            "Ones": Ones,
            "Twos": Twos,
            "Threes": Threes,
            "Fours": Fours,
            "Fives": Fives,
            "Sixes": Sixes,
            "Three Of A Kind": ThreeOfAKind,
            "Four Of A Kind": FourOfAKind,
            "Full House": FullHouse,
            "Small Straight": SmallStraight,
            "Large Straight": LargeStraight,
            "Yahtzee": Yahtzee,
            "Chance": Chance
    }

    def get_total_points(self):
        """ Get total points """
        pos_sum=0
        for value in self.points.values():
            if value>0:
                pos_sum+=value
        return pos_sum

    def add_points(self, rule_name, hand):
        """ Add points """
        my_obj=self.dict_class[rule_name]
        #print("*********")
        #print(type(hand))
        #print(hand)
        #print("*********")
        if self.points[rule_name]==-1:
            self.points[rule_name]=my_obj.points(hand,hand)
        else:
            raise ValueError("Redan vald!")

    def get_points(self, rule_name):
        """ Get points """
        my_obj=self.points[rule_name]
        return my_obj

    def finished(self):
        """ Check if finished """
        if -1 in self.points.values():
            return False
        return True

    @classmethod
    def from_dict(cls,points=None):
        """ Get from dict """
        if points is None:
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
        sb=cls(points)
        return sb
