from src.die import Die

class Hand():
    #dice=list[Die]

    def __init__(self,dice_values=None):
        self.dice=[]
        for x in range(5):
            #die=Die()
            self.dice.append(Die())

    def roll(self,my_list=None):
        if my_list==None:
            my_list=[0,1,2,3,4]
        for x in range(5):
            die=Die()
            #tarn=die.roll()
            if x in my_list:
                #print(x)
                self.list[x]= die
    
    def __str__(self):
        strang=""
        for x in range(5):
            die=self.dice[x]
            strang+=str(die)+", "
        return strang[:len(strang)-2]

    def dice_name(self):
        strang=""
        for x in range(5):
            die=self.list[x]
            strang+=str(die.get_name())+", "
        return strang[:len(strang)-2]