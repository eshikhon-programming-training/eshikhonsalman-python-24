class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname,self.lname,self.gender)

class Student(Person):

    def __init__(self,fname,lname,gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    # def print(self):
    #     print(self.fname,self.lname,self.gender)
obj1 = Student('salman','sultan','male')

obj1.print()

#implement inheritance concept with two practical example