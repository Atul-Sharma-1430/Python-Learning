#OOP2

# # del Keyword --> Used to delete object properties or Object itself
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Atul");
# print(s1.name);
# del s1
# print(s1.name);  # --> Gives error


# #Private(like) attributes and methods
# #Privatre attributes and methods can be used within the class not outside it
# class Account:
#     def __init__(self, accNo, accPass):
#         self.accNo = accNo
#         self.__accPass = accPass   # --> Way to make private just add 2 __ .

#     def resetPass(self):
#         print(self.__accPass) # --> Here within the class it is accessible but not outside

#     def __privMethod(self):  # --> Private method
#         print("This is a private method.")

#     def callPrivMethod(self):   # --> function to call private method
#         self.__privMethod()

# a1 = Account("1001" , "ABCDE")
# # print(a1.accNo, a1.__accPass)  # --> Here not accessible
# a1.resetPass()
# a1.callPrivMethod()




# #Inheritance --> One class extends the attributes of other class
# class Car:
#     @staticmethod
#     def start():
#         print("Car is Starring....Bruhhhh")

#     @staticmethod
#     def stop():
#         print("Car Stopped")


# class Toyota(Car):
#     def __init__(self , name):
#         self.name = name

#     def start(self):
#         print("Car is Starting.....BROOMBROOM")

# car1 = Toyota("Supra1")
# car2 = Toyota("Supra2")
# car1.start()


# #Types of Inheritance

# #1.Single level Inheritance --> Above example

# #2.Multilevel Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car is Starring....Bruhhhh")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class Toyota(Car):
#     def __init__(self , brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self , type):
#         self.type = type

# car1 = Toyota("Diesel")
# car1.start()


# #3.Multiple Inheritance
# class A:
#     varA = "I am in Class A"

# class B:
#     varB = "I am in class B"

# class C(A,B): #--> Multiple Inheritance
#     varC = "I am in class C. I have property of both class A and B"

# c1 = C()
# print(c1.varA)




# #Super Method --> Used to acccess methods of parent class, super().
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car is Starring....Bruhhhh")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class Toyota(Car):
#     def __init__(self , name, type):
#         super().__init__(type)   # --> !!! Calling parent methods and passing its value
#         self.brand = name

# c1 = Toyota("Supra", "EV")
# print(c1.type)




# #Class Method or Decorator
# #A class method is bound to the class and recieves the class as an implicit argument
# #Since static methods can't access or modify class state and generally used for utility hence we use class methods


# #Simple Ways to change class variable
# class Person:
#     name = "Anonymous"

#     def changeName(self , name):
#         self.name = name           # --> This change the name of its object only
#         Person.name = name         # --> This changes the name of the class variable
#         self.__class__.name = name # --> This also changes the name of the class variable

# p = Person()
# p.changeName("Atul")
# print(p.name)            # --> Gives name as Atul
# print(Person.name)       # --> Also Gives name as Atul 


# #Way to change class variable using Class Method
# class Person:
#     name = "Anonymous"

#     @classmethod                # ---> This is used to make class method
#     def changeName(clss, name):
#         clss.name = name           
       
# p = Person()
# p.changeName("Atul")     # --> changing name through object but class variable name changes
# print(Person.name)
 




# #Property Decorator --> Used to decorate any method in the class to use it as a property
# class Student:
#     def __init__(self , phy , chem , maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths

#     @property
#     def calPerc(self):
#         return str((self.phy + self.chem + self.maths) / 3) + "%"

# s1 = Student(67, 82, 98)
# print(s1.calPerc)


#!!! Getter and Setter are also decorators





# #Polymorphism
# #1.Operator overloading -- >Diff operator works diff according to context.
# print(1 + 2) #3
# print("Atul" + "Sharma") # Atul Sharma
# print([1,2,3] + [4,5,6]) # [1,2,3,4,5,6]


# #Creating a complex number class
# class Complex:
#     def __init__(self , real , img):
#         self.real = real
#         self.img = img

#     def showNum(self):
#         print(self.real , "i + (" , self.img , "j)")

#     #Method 1 to calculate or normally without using Dunder functions
#     def add(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     #Dunder Function for Add
#     def __add__(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     #Dunder Function for Sub
#     def __add__(self , num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
#     #And many more .....

# # --> now to add above those numbers as complex numbers we use "Dunder functions"
# # --> To define any meaning of a operator as operator overloading we use "Dunder functions"(__)

# num1 = Complex(1,3)
# num1.showNum()

# num2 = Complex(10,9)
# num2.showNum()

# #Calling method 1 but we dont want to call it as a function we want to use it normally so use DF
# ans = num1.add(num2)
# ans.showNum()

# #Calling DF
# ans = num1 + num2 # Here we have called without function just like normal adddition.
# ans.showNum()



# #Q: Define a Circle class to create a circle with raduis using const
# #   Define area and perimeter method for circle
# class Circle:
#     def __init__(self , rad):
#         self.rad = rad

#     def area(self):
#         print("Area of circle is", (22/7) * (self.rad ** 2), "sq unit")
#         return (22/7) * (self.rad ** 2)
    
#     def perimtr(self):
#         print("Perimeter of circle is", 2 * (22/7) * self.rad, "units")
#         return 2 * (22/7) * self.rad
    
# c1 = Circle(9.6)
# c1.area(); c1.perimtr()


# #Q: Define Employee class with att role, dept and salary and a methos showDetails()
# #   Create an engineer class that inherits props from employee and has additional att name n age
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role:", self.role)
#         print("Salary:", self.salary)
#         print("Dept:", self.dept)
        

# class Engineer(Employee):
#     def __init__(self, role, dept, salary, name, age):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age

# raj = Engineer("HR", "IT", "60k", "Raj", 40)
# raj.showDetails()


# #Q: Create a class called order which stores item and its price
# #   Use dunder function__gt__() to convey that: o1 > 02 if prince of o1 > o2
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, order2):
#         return self.price > order2.price


# o1 = Order("Tea", 15)
# o2 = Order("Coffee", 20)

# print(o1 > o2)   





