from src.die import Die
from src.hand import Hand

dice1=Die()
dice1.roll()
print(dice1)
print(dice1.get_name())
hand=Hand()
print(hand)
hand.roll()
print(hand)
hand.roll([4,2])
print(hand)
dice3=Die(50)
print(dice3)
