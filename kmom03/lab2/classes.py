class Person():
    def __init__(self, name, ssn, address=""):
        self.name=name
        self._ssn=ssn
        self.address=str(address)
    
    def set_address(self, city, state, country):
        self.address=Address(city,state,country)

    def get_ssn(self):
        return self._ssn
    
    def __str__(self):
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn
        else:
            return "Name: "+self.name+" SSN: "+self._ssn+self.address

class Address():
    def __init__(self, city, state, country):
        self.city=city
        self.state=state
        self.country=country
    
    def __str__(self):
        return " Address: "+self.city+" "+self.state+" "+ self.country

class Teacher(Person):
    def __init__(self,name,ssn,address=""):
        self.courses=[]
        super(Teacher, self).__init__(name,ssn,address)
    
    def add_course(self,course):
        self.courses.append(course)

    def __str__(self):
        courses_str=""
        for course in self.courses:
            courses_str+=course+", "
        courses_str=courses_str[:len(courses_str)-2]
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn+" Courses: "+courses_str
        else:
            return "Name: "+self.name+" SSN: "+self._ssn+self.address+" Courses: "+courses_str

class Student(Person):
    def __init__(self,name,ssn,address=""):
        self.courses_grades=[]
        super(Student, self).__init__(name,ssn,address)
    
    def add_course_grade(self,course,grade):
        self.courses_grades.append(tuple((course,grade)))

    def average_grade(self):
        sum=0
        number=0
        for x in range(len(self.courses_grades)):
            if self.courses_grades[x][1]!="-":
                sum+=int(self.courses_grades[x][1])
                number+=1
        return sum/number

    def __str__(self):
        if self.address=="":
            return "Name: "+self.name+" SSN: "+self._ssn+" Courses with grades: "+str(self.courses_grades)
        else:
            return "Name: "+self.name+" SSN: "+self._ssn+self.address+" Courses: "+str(self.courses_grades)