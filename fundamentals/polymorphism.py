#function_Based_polymorphism

name = "salman"
product =[1,2,3]

print(len(name))
print(len(product))

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

obj1 = Car('A1','B1')
obj2 = Plane('A2','B2')

for i in (obj1,obj2):
    i.move()
