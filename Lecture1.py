# #Outpt
# print("Hello Atul Sharma.");

# #Variables
# name = "Atul";
# age = 20;
# rollNo = 42;
# num = 25.98;
# a = None; # N should be capital
# isValid = False; # F and T should be Capital
# print(name, age, rollNo, num);

# #type() --> Gives the type of the data.
# print(type(name));   # --> <class 'str'>
# print(type(age));    # --> <class 'int'>
# print(type(rollNo)); # --> <class 'int'>
# print(type(num));    # --> <class 'float'>
# print(type(a));      # --> <class 'NoneType'>
# print(type(isValid));# --> <class 'bool'>


# #Sum of Two nums
# num1 = 25;
# num2 = 35;
# print("The sum of", num1, "and", num2, "is", num1 + num2); #Formatting

# #Comments.
# # -->  Used for single line comment
# # --> """ This is used for multi line comments """


# #Arithmetic Operators
# number1 = 5;
# number2 = 2;
# print(number1 + number2);
# print(number1 - number2);
# print(number1 * number2);
# print(number1 / number2); # --> Gives ans as 2.5 bcz python always does floating division.
# print(number1 ** number2); # --> means 5 raised to 2 = 25.
# print(number1 % number2);

# #Relational Operator
# x = 20;
# y = 30;
# print(x == y);
# print(x != y);
# print(x > y);
# print(x < y);
# print(x >= y);
# print(x <= y);

# #Assignment Operator
# m = 10;
# m += 5;
# m *= 5;
# m /= 5;
# m -= 5;
# m **= 2;
# m %= 3;


# #Logical Operator
# val1 = True;
# val2 = False;
# print("AND operator:", val1 and val2);
# print("OR operator:", val1 or val2);
# print("NOT operator:", val1 and not(val2));


# #Type Conversion(Implicit) & Casting(Explicit)
# n1 = int("15");
# n2 = 10;
# print("Sum is", n1 + n2);
# print(type(n1));


# #Input from user
# naam = input("Enter your name");
# print("Your name is", naam);
# z1 = int(input("Enter a number:"));# --> Here in python if we take input from user it always takes it as String so we need to type cast it
# print(type(z1), z1); # --> Type will be int.
# z2 = input("Enter a number:");
# print(type(z2), z2); # --> Type will be String by default.


# #Q1: Program to input 2 nums and print their sum
# v1 = int(input("Enter first number: "));
# v2 = int(input("Now, Enter the second number: "));
# print("The sum of", v1 , "and", v2 , "is", v1+v2);


# #Q2: Print area of a Square
# side = float(input("Enter the side of the Square: "));
# print("The area of the Square is:", side ** 2);

# #Q3: Average of two numbers
# first = float(input("Enter first number: "));
# second = float(input("Now, Enter the second number: "));
# print("The Average of", first , "and", second , "is", (first+second)/2);










print("Atul", end = " ",)
print("sharma")
#Above the output will be in same line cz we have passed the value of end as " " and inbuilt it is written asn "\n" 
#but we have overwritten it. We can paass any value 