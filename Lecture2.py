# #Strings
# #Different ways to write String.
# str1 = "This is the second lecture of python"; # length = (36)
# str2 = 'This is the second lecture of python';
# str3 = """This is the second lecture of python""";
# str4 = '''This is the second lecture of python''';


# print(len(str1)); # --> Gives the length of the String.


# #Concatenation (+)
# print(str1 + str2 + str2); #--> does not adds space by its own
# print(str1 , str2 , str3); # --> adds space by its own
# newStr = str1 + " " + str2; # --> This is also possible in python.
# print(len(newStr)); # --> counts the space also.(73)


# #Indexing
# # H E L L O
# # 0 1 2 3 4
# print(str1[25]); #We can acces it but cannot change because Strings are Immutable
# # str1[25] = "A"; --> This is not possible


# #Slicing 
# #str[start_index : last_index], Last index is not counted
# print(str1[2 : 24]); # --> is is the second lectu
# print(str1[ : 24]);  # --> Here starting index is considered as 0.
# print(str1[2 : ]);   # --> Here last index is considered as len(str).


# #Negative Indexing of String
# #  H    E   L   L   O
# # -5   -4  -3  -2  -1
# greet = "Hello";
# print(greet[-5 : -1]); # --> Hell


# #String Functions (Imps only)
# str = "i am Atul Sharma.";

# print(str.endswith("arma.")); # --> True
# print(str.endswith("Arma.")); # --> False, bcz case sensitive

# print(str.capitalize()); # --> Capitals the first letter. i --> I

# print(str.replace("Atul", "Aditya")); # --> Replaces all Occurance of the letter or word it doesnot changes original String
# print(str); # --> Here the string will be same as original one.

# print(str.find("a")); # --> Returns the first index of first occurance of letter or word (2).
# print(str.find("Atul")); # return 5
# print(str.find("atul")); # returns -1

# print(str.count("a")); # --> count occurance of substring in a string (3).
# print(str.count("Atul")); # return 1
# print(str.count("atul")); # returns 0

# #Q1: Takes users name as input and print its length.
# name = input("Enter your name: ");
# print("Your name is", name , "and the length of your name is", len(name), ".");

# #Q2: Write a Program to find the occurance of $ in a String.
# string = input("Enter the String having ($) sign in it: ");
# print("Your String has", string.count("$"), "$'s in it.");



#*********************************************************************************#



# #Conditional Statements
# age = 20;
# if(age < 18):
#     print("You are not Eligible to drive"); #Indentation
# elif(age < 60):
#     print("You can Drive.");
# else:
#     print("You cannot Drive");


# #Q3: Program to give Grade based in Marks
# marks = int(input("Enter your marks(1-100):"));
# if(marks < 1 or marks > 100):
#     print("Enter a Valid marks.");
# elif(marks >= 90):
#     print("Grade A");
# elif(marks >= 80):
#     print("Grade B");
# elif(marks >= 60):
#     print("Grade C");
# elif(marks >= 35):
#     print("Grade D");
# else:
#     print("FAIL");


# #Nesting 
# age = 95;
# if(age >= 18):
#     if(age >= 80):
#         print("Cannot Drive");
#     else:
#         print("Can Drive");
# else:
#     print("Cannot Drive")
    

# #Q4:Odd even Number
# num = int(input("Enter the Number:"));
# if(num % 2 == 0):
#     print(num, "is an Even Number");
# else:
#     print(num, "is and Odd Number");

# #Q5:Greatest of 4
# first = int(input("Enter first number: "));
# second = int(input("Enter second number: "));
# third = int(input("Enter third number: "));
# four = int(input("Enter fourth number: "));
# if(first > second and first > third and first > four):
#     print(first, "is the largest number.");
# elif(second > third and second > four):
#     print(second, "is the largest num");
# elif(third > four):
#     print(third, "is the largest num");
# else:
#     print(four, "is the largest num");


# #Q6:Check the number is multiple of 7 or not
# num = int(input("Enter the number:"));
# if(num % 7 == 0):
#     print(num, "is a multiple of 7.");
# else:
#     print(num, "is not a multiple of 7.")