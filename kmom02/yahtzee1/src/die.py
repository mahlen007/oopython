import random

class Die():
    MIN_ROLL_VALUE=1
    MAX_ROLL_VALUE=6
    
    def __init__(self):
        self._value=random.randint(1,6)
    
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
        side=random.randint(1,6)
        self._value=side
        return side
    
    def __str__(self):
        return str(self._value)