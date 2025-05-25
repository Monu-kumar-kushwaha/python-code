# class Student:  #class
#     name = "virat"
    
# s1 = Student  #object
# print(s1.name)

# s2 = Student
# print(s2.name)

# class car:
#     color ="blue"
#     brand = "merscdes"

# car1 = car
# print(car1.color)
# print(car1.brand)

#__init__ function

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")

# s1 = Student("rohit", 87)
# print(s1.name,s1.marks)

# s2 = Student("virat",98)
# print(s2.name,s2.marks)    
    
# #class & instance Attribute

# class Student:
#     college_name = "ABCcollege"
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")

# s1 = Student("karan",86)
# print(s1.name, s1.marks)

# s2 = Student("aarav",98)
# print(s2.name, s2.marks)

# print(Student.college_name)

# # method
# # method are function that belong to objects.


# class Student:
#     college_name = "ABC college"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("guddu", 96)
# s1.welcome()
# print(s1.get_marks())

# class Student:
#      def __init__(self,name,marks):
#          self.name = name
#          self.marks = marks

#      def get_avg(self):
#          sum = 0
#          for val in self.marks:
#              sum += val
#          print("Hi", self.name,"your avg score is :",sum/3)

# s1 = Student("tony stark", [98,87,95])
# s1.get_avg()

# s1.name = "ironman"  #change value
# s1.get_avg()

# s1.marks = [87,67,98]
# s1.get_avg()

# #Statics method

# class Student:  #only for class method
#     @staticmethod
#     def college():
#         print("ABC college")
       

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "was credited")
#         print("Total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(50000)
# acc1.debit(10000)

#del keyword
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("rahul")
# print(s1.name)
# del s1.name
# print(s1.name)

#private attributes and method

# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person !")

#     def welcome(self):
#         self.__hello()

# p1 = person()
# print(p1.welcome)

#inheritance
#single inheritance
class car:
    colour = "black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(car):
    def __init__(self, name):  # Corrected __int__ to __init__
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.colour)  # Corrected color() to colour

#multi - level inheritance

class car:              #parent
     @staticmethod
     def start():
         print("car started..")

     @staticmethod
     def stop():
         print("car stoped")

class toyotacar(car):          #parent
    def __init__(self,brand):
        self.brand = brand

class fortuner(toyotacar):       #child
    def __init__(self,type):
        self.type = type

car1 = fortuner("diesel")
car1.start()

# multiple inheritance

class A:  #PARENT CLASS 
    varA = "welcome to class A"
class B:   #PARENT CLASS 
    varB = "welcome to class B"
class C(A,B):    #CHILD CLASS
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#super method

class car:
    def __init__(self ,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = toyotacar("fortuner","electric")
print(car1.type)


#class method
class person:
    name = "anomymous"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("aryan")
print(p1.name)
print(person.name)

#property
class Student:
    def __init__(self,phy,chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy +self.chem + self.math)/3) +'%' 
        
stu1 = Student(97,87,88)
print(stu1.percentage)

stu1.phy = 85  #change value
print(stu1.percentage)

#polymorphism

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i", self.img, "j")

    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal, newimg)

# Instantiate objects and perform operations outside the class definition
num1 = complex(2, 6)
num1.shownumber()

num2 = complex(4, 7)
num2.shownumber()

num3 = num1 - num2  #(a+b),(a-b),(a*b),(a/b),(a%b)
num3.shownumber()


#let's practice

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating an instance of Circle and printing the area and perimeter
c1 = Circle(21)
print(c1.area())       # Correct method call with parentheses
print(c1.perimeter())  # Correct method call with parentheses


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        super().__init__("engineer", "IT", "60,000")

engg1 = Engineer("elon musk", 30)
engg1.showdetails()  # Correct way to call the showdetails method on the instance


class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea",15)

print(odr1 > odr2)





