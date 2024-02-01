class Rule():
    pass

class ThreeOfAKind(Rule):
    def __init__(self):
        self.name = "Three of a kind"
    
    def points(self,hand):
        pass

class FourOfAKind(Rule):
    def __init__(self):
        self.name = "Four of a kind"
    
    def points(self,hand):
        pass

class FullHouse(Rule):
    def __init__(self):      
        self.name = "Full house"
    
    def points(self,hand):
        pass

class SmallStraight(Rule):
    def __init__(self):
        self.name = "Small straight"
    
    def points(self,hand):
        pass

class LargeStraight(Rule):
    def __init__(self):
        self.name = "Large straight"
    
    def points(self,hand):
        pass

class Yahtzee(Rule):
    def __init__(self):
        self.name = "Yahtzee"
    
    def points(self,hand):
        pass

class Chance(Rule):
    def __init__(self):
        self.name = "Chance"
    
    def points(self,hand):
        pass


class SameValueRule(Rule):
    def __init__(self, value, name):
        self.name=name
        self.value=value
    
    def points(self, hand):
        pass

class Ones(SameValueRule):
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    def __init__(self):
        super().__init__(6, "Sixes")        