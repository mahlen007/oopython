import random

class Die():
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    #_value=1
    
    def __init__(self,value=None):
        #print(Die.MAX_ROLL_VALUE)
        if value==None:
            value=random.randint(1,6)
        elif value<Die.MIN_ROLL_VALUE:
            value=Die.MIN_ROLL_VALUE
        elif value>Die.MAX_ROLL_VALUE:
            value=Die.MAX_ROLL_VALUE
        self._value=value
    
    def get_name(self):
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

    def get_value():
        return _value
    
    def roll(self):
        side=random.randint(Die.MIN_ROLL_VALUE,Die.MAX_ROLL_VALUE)
        self._value=side
        return side
    
    def __str__(self):
        return str(self._value)