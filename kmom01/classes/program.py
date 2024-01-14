import random
class Coin:
    def __init__(self):
        self.sideup="head"

    def toss(self):
        slump=random.randint(0,1)
        if slump==0:
            return "head"
        else:
            return "tail"

mynt1 = Coin()
mynt1.sideup=mynt1.toss()
print(mynt1.sideup) 