# OOP1

# #Creating class
# class Student :
#     collgName = "Tcet" # --> Class member
#     def __init__(self, name): # -- > Constructor
#         print("Constructor called")
#         self.name = name

#     def greet(self):  # -- > Method
#         print("Good Morning")

#     def getName(self) :
#         return self.name;


# stud1 = Student("Atul");
# print(stud1) # --> <__main__.Student object at 0x000001CA7BD770E0>
# print(stud1.name);

# stud2 = Student("Aditya")
# print(stud2.name);
# stud2.greet();
# print(stud2.getName())


#Constructor  -->  All classes hasve a function called _init_(), which is always executed when the object is created
#Self --> We always need to write in the in constructor or in methods defines in that class. it works as this keyword in java. we can use any other name also
#Class attributes == Static members of java
#Instance attributes == Non static members of java   !! Obj att >> class att



#Methods --> Same as java

# # Q1: Create student class that takes name and marks of 3 subjects in const then a method ro print avg
# class Student :
#     def __init__(self, name, eng, maths, hindi):
#         self.name = name
#         self.eng = eng
#         self.maths = maths
#         self.hindi = hindi

#     def calAvg(self) :
#         return (self.eng + self.maths + self.hindi) / 3;

# s1 = Student("Atul Sharma",100,90,87)
# print(s1.calAvg());



# #Static methods 
# #Sattic methods are  those methods that dont use "self" parameter and work on class level
# class Car:
#     @staticmethod  # --> Decorator : Changes the behaviour of a function
#     def greetcust() :  # --> No self param
#         print("Welcome to the ShowRoom Sir..!!")

# c1 = Car();
# c1.greetcust()


# #Abstraction --> Hinding the implementation details of a class and only showing the imp features to user by making it private
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.acc = True
#         self.brk = True
#         self.clutch = True
#         print("Car Statrted")

# c1 = Car();
# c1.start(); # --> Here while starting we dont neet to worry about how it started all hidden means abstraction


# # Encapsulation --> Wrapping data and function into a single object(unit)
# # It basically the same what we are doing in classes n objects like makeing a class and then grouping att and methods based on diff objects


# #Q2: Create account class with 2 attributes calance and acc no.create methods for debit credit and printing balance
# class Account:
#     def __init__(self, accNo, balance):
#         self.accNo = accNo
#         self.balance = balance

#     def debit(self, amount):
#         if self.balance < amount:
#             print("Account balance is low, cannot debit money.")
#         else:
#             self.balance -= amount
#             print(amount, "rs debited from account number", self.accNo,
#                   ", remaining balance:", self.check_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print(amount, "rs credited to account number", self.accNo,
#               ", updated balance:", self.check_balance())

#     def check_balance(self):
#         print("Your account balance is", self.balance, "rs.")
#         return self.balance


# a1 = Account(10, 100)
# a1.credit(500)
# a1.debit(300)
# a1.check_balance()
