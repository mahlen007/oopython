"""
Classes for lab 2
"""
class Person():
    """ Person class """
    def __init__(self, name, ssn, address=""):
        self.name=name
        self._ssn=ssn
        self.address=str(address)

    def set_address(self, city, state, country):
        """ Set Adress """
        self.address=Address(city,state,country)

    def get_ssn(self):
        """ Get ssn """
        return self._ssn

    def __str__(self):
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn
        return "Name: "+self.name+" SSN: "+self._ssn+self.address

class Address():
    """ Address class """
    def __init__(self, city, state, country):
        self.city=city
        self.state=state
        self.country=country

    def __str__(self):
        return " Address: "+self.city+" "+self.state+" "+ self.country

class Teacher(Person):
    """ Teacher class """
    def __init__(self,name,ssn,address=""):
        self.courses=[]
        super().__init__(name,ssn,address)

    def add_course(self,course):
        """ Add course """
        self.courses.append(course)

    def __str__(self):
        courses_str=""
        for course in self.courses:
            courses_str+=course+", "
        courses_str=courses_str[:len(courses_str)-2]
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn+" Courses: "+courses_str
        return "Name: "+self.name+" SSN: "+self._ssn+self.address+" Courses: "+courses_str

class Student(Person):
    """ Student class """
    def __init__(self,name,ssn,address=""):
        self.courses_grades=[]
        super().__init__(name,ssn,address)

    def add_course_grade(self,course,grade):
        """ Add course grade """
        self.courses_grades.append(tuple((course,grade)))

    def average_grade(self):
        """ Calculate average grade """
        my_sum=0
        number=0
        #for x in range(len(self.courses_grades)):
        for x, _ in enumerate (self.courses_grades):
            if self.courses_grades[x][1]!="-":
                my_sum+=int(self.courses_grades[x][1])
                number+=1
        return my_sum/number

    def __str__(self):
        if self.address=="":
            return ("Name: "+self.name+" SSN: "+self._ssn+" Courses with grades: " +
            str(self.courses_grades))
        return ("Name: "+self.name+" SSN: "+self._ssn+self.address+" Courses: " +
        str(self.courses_grades))
