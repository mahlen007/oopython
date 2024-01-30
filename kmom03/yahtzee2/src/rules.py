class Rule():
    list_of_value=[0,0,0,0,0,0]

    def points(self, hand):
        pass
    
    def count_dice(self, hand):
        for die in hand:
            list_of_value[die.get_value()-1]+=1

class ThreeOfAKind(Rule):
    def __init__(self):
        self.name = "Three of a kind"
    
    def points(self,hand):
        self.count_dice(hand)
        test=False
        points=0
        for x in range(6):
            points+=list_of_value[x]*(x+1)
            if list_of_value[x]>=3:
                test=True
        if test:
            return points
        else
            return 0

class FourOfAKind(Rule):
    def __init__(self):
        self.name = "Four of a kind"
    
    def points(self,hand):
        self.count_dice(hand)
        test=False
        points=0
        for x in range(6):
            points+=list_of_value[x]*(x+1)
            if list_of_value[x]>=4:
                test=True
        if test:
            return points
        else
            return 0        

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
        self.count_dice(hand)
        test=False
        points=0
        for x in range(6):
            points+=list_of_value[x]*(x+1)
            if list_of_value[x]==5:
                test=True
        if test:
            return 50
        else
            return 0  

class Chance(Rule):
    def __init__(self):
        self.name = "Chance"
    
    def points(self,hand):
        points=0
        for die in hand:
            points += die.get_value()
        return points
    
class SameValueRule(Rule):
    def __init__(self, value, name):
        self.name=name
        self.value=value
    
    def points(self, hand):
        points=0
        for die in hand:
            if die.get_name() == self.name:
                points+=die.get_value()
        return points

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