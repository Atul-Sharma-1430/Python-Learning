#Loops in Python

# #1: While Loop
# i = 1;
# while i <= 5 :
#     print("Hello", i);
#     i += 1;

# #Q1 : 1-100 nums
# i = 1;
# while i <= 100 :
#     print(i);
#     i += 1;

# #Q2 : 100-1 nums
# i = 100;
# while i >= 1 :
#     print(i);
#     i -= 1;

# #Q3 : Multiplication table of a number n
# num = int(input("Enter a number:"));
# i = 1;
# while i <= 10 :
#     print(num, "X", i, "=", num*i);
#     i += 1;

# #Q4 : Print elements of list using Loop
# nums = [1,2,3,4,5,6,8,23,45,67,89]
# i = 0;
# while i < len(nums) :
#     print(nums[i]);
#     i += 1;

# #Q5 : Search a number in a tuple using loop
# nums = (1,2,3,4,5,6,8,23,45,67,89)
# target = 89;
# i = 0;
# while i < len(nums) :
#     if(nums[i] == target) :
#         print("Targer found at index", i);
#         break;
#     else :
#         print("Searching....")
#     i += 1;


#*********************************************************************************#


# #2. For Loops

# #1. --> Kind of For-each Loop in java.
# list1 = [1,2,3,4,5]
# for val in list1 :
#     print(val);

# str = "Atul Sharma"
# for char in str :
#     print(char);


# #2. --> For Loop with else.
# tup = (1,2,3,4,5)
# for val in tup :
#     print(val);
# else :
#     print("Loop ends here.")


#Range Function.
#Range Function returns a sequence of numbers, starting from 0 by default and increments by 1 by default and stops before a specified number.
#Example: range(6) = 0,1,2,3,4,5
#Syntax : range(start?, stop, step?)


# #Method 1 to write Range Function
# for elem in range(5) :
#     print(elem);                     # --> 0,1,2,3,4

# #Method 2 to write Range Function
# for elem in range(2 , 5) :
#     print(elem);                     # --> 2,3,4

# #Method 3 to write Range Function
# for elem in range(1 , 10 , 2) :
#     print(elem);                     # --> 1,3,5,7,9



# #Q: Print numbers 1-100 using range 
# for num in range(1,101) :
#     print(num);

# #Q: Print numbers 100-1 using range 
# for num in range(100,0,-1) :
#     print(num);

# #Q: Multiplication table of a num
# num = int(input("Enter the number:"))
# for i in range(1 , 11 , 1) :
#     print(num, "X", i, "=", num*i)


# #Pass Statement.
# #Pass is a null statement that does nothing. It is used as a placeholder for furute code. we can use in if-else also
# for val in range(10) :
#     pass

# print("Loop ends after pass")


# #Q : Sum of first n numbers using While
# terms = int(input("Enter the number of terms whose sum is to be printed:"))
# i = 1; sum = 0;
# while i <= terms :
#     sum += i;
#     i += 1;
# print("Sum of first", terms , "natural numbers is", sum)

# #Q: factorial of number using for
# num = int(input("Enter the number:"))
# fact = 1
# for i in range(1 , num+1) :
#     fact *= i;

# print("facctorial of", num , "is", fact)