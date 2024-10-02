class Animal:
    tail =''
    eyes=''
    leg=''
    def __init__(self,x,y,z):
        self.tail = x
        self.eyes = y
        self.leg=z
        print(self.tail,self.eyes,self.leg)
    def activity(self):
        return "biral ghumary"


no_of_tail = 1
no_of_eyes = 2
no_of_leg = 4
cat = Animal(no_of_tail,no_of_eyes,no_of_leg) #class er instance
human = Animal(0,2,2)
# # tiger = Animal() #class er instance

# # cat.name = 'biral'

# # print(cat.activity())
