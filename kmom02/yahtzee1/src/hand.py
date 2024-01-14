from src.die import Die

class Hand():
    list=[]

    def __init__(self):
        for x in range(5):
            #die=Die()
            self.list.append(Die())

    def roll(self):
        for x in range(5):
            die=Die()
            #tarn=die.roll()
            self.list.insert(x, die)
    
    def __str__(self):
        strang=""
        for x in range(5):
            die=self.list[x]
            strang+=str(die)+", "
        return strang[:len(strang)-2]
