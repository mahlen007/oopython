""" Tester """
from src.hand import Hand
from src.rules import Ones, Twos, Chance, Yahtzee, LargeStraight, \
        SmallStraight, FullHouse,FourOfAKind
from src.scoreboard import Scoreboard

hand1=Hand([6,6,6,6,6])
#print(hand1.to_list())

o=Ones()
t=Twos()
c=Chance()
y=Yahtzee()
ls=LargeStraight()
ss=SmallStraight()
fh=FullHouse()
fok=FourOfAKind()
print(ss.points(Hand([1,2,3,4,2])))
a_dict={
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
o = Scoreboard.from_dict(a_dict)
print(o)

#print(hand1)
