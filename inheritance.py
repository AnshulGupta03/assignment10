#Q.1- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        print("They have 4 legs.")
        print("They are carnivores.")

class Tiger(Animal):
    pass

x = Tiger()
x.animal_attribute()

print("\n\n",10*"*")




#Q.2- What will be the output of following code.
'''
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
'''

#OUTPUT- A B

print("\n\n",10*"*")





#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
#Define methods to add, display and update the following details. Create another class Mission which extends the class Cop.
#Define method add_mission_details.
#Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.


class Cop:
    def __init__(self,name,age,work_exp,designation):
        self.name = name
        self.age = age
        self.work_exp = work_exp
        self.designation = designation

    def add(self,gender):
        self.gender = gender

    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("gender: ",self.gender)
        print("work experience: ",self.work_exp)
        print("designation: ",self.designation)

    def update(self,age):
        self.age = age


class Mission(Cop):
    def add_mission_details(self,topic,duration):
        self.topic = topic
        self.duration = duration
        print("The following cop has to go on %s mission for %d days."%(self.topic,self.duration))


m1= Mission('Anmol',28,5,'Sub inspector')
m1.add_mission_details('26 jan',30)
m1.add('male')
m1.update(29)
m1.display()


print("\n\n",10*"*")




#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.


class Shape:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        if (self.length == self.breadth):
            self.shape = 'square'
        else:
            self.shape = 'rectangle'
            
        print ("area of %s= "%(self.shape
                               ),self.length * self.breadth)

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

r = Rectangle(3,4)
r.area()
s = Square(3,3)
s.area()


print("\n\n",10*"*")





