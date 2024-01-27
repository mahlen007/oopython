class Person():
    def __init__(self, name, ssn, address=""):
        self.name=name
        self._ssn=ssn
        self.address=address
    
    def set_address(self, city, state, country):
        self.address=Address(city,state,country)

    def get_ssn(self):
        return self._ssn
    
    def __str__(self):
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn
        else:
            address=self.address
            #print(type(address))
            return str("Name: "+self.name+" SSN: "+self._ssn)+self.address.__str__()

class Address():
    def __init__(self, city, state, country):
        self.city=city
        self.state=state
        self.country=country
    
    def __str__(self):
        return " Adress: "+self.city+" "+self.state+" "+ self.country

class Teacher(Person):
    def __init__(self):
        self.courses=[]
    
    def add_course(self,course):
        self.courses.append(course)
