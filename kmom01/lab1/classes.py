"""
Modul med klasser.
"""
class Cat():
    """
    En class med katt.
    """
    nr_of_paws=4

    def __init__(self, eye_color, name):
        self.eye_color=eye_color
        self.name=name
        self.lives_left=-1

    def description(self):
        """
        Beskrivning av en katt.
        """
        strang=f"My cat's name is {self.name}, has {self.eye_color} eyes"
        strang+=f" and {self.lives_left} lives left to live."
        return strang

class Duration():
    """
    En class om tid.
    """
    def __init__(self, hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def display(self):
        """
        Ger en snygg utskrift.
        """
        hh=str(self.hours)
        if self.minutes<10:
            mm="0"+str(self.minutes)
        else:
            mm=str(self.minutes)
        if self.seconds<10:
            ss="0"+str(self.seconds)
        else:
            ss=str(self.seconds)

        return hh+"-"+mm+"-"+ss

    def duration_to_sec(self, tid):
        """
        Gör om till sekunder.
        """
        tim=int(tid[:2])
        min_=int(tid[3:5])
        sek=int(tid[6:])
        return tim*3600+min_*60+sek

    def __add__(self, other):
        """
        Adderar 2 tider.
        """
        if self.seconds+other.seconds>59:
            self.seconds=(self.seconds+other.seconds)%60
            self.minutes+=1
        else:
            self.seconds=self.seconds+other.seconds
        if self.minutes+other.minutes>59:
            self.minutes=(self.minutes+other.minutes)%60
            self.hours+=1
        else:
            self.minutes=self.minutes+other.minutes
        self.hours=self.hours+other.hours
        return self

    def __shorter__(self,other):
        """
        Jämför längden på två tider.
        """
        sec1=self.hours*3600+self.minutes*60+self.seconds
        if sec1<other.hours*3600+other.minutes*60+other.seconds:
            return True
        return False
