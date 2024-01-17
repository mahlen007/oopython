from ..src.die import Die

#Tester
#Att skapa ett objekt utan skicka argument till konstruktorn.
die1 = Die()

#Att skapa ett objekt och skicka värde på tärningen till konstruktorn.
die2 = Die(3)

#Att skapa ett objekt och skicka ett otillåtet värde på tärningen, som till exempel 100, till konstruktorn.
die3 = Die(100)
die3.roll()
die3.get_name()

