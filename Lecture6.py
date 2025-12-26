#Functions
#Block is code that performs a specefic task
#Syntax :- def func_name(params) :

# def calSum(num1 , num2) :
#     return num1 + num2;

# sum = calSum(3 , 10);
# print(sum);



# #Default arguments

# def calMul(a = 1, b = 2) :
#     print( a * b );
# calMul(); # --> It will not give error cz we have set Defalt argms.

# def calMul(a , b = 2) :  # --> This is allowed.
#     print( a * b );

# # def calMul(a = 1, b) : # --> This is not allowed keeping 2nd param as non-default.
# #     print( a * b );



# cities = ["A", "B", "C", "D", "E"]
# villages = [1, 2, 3, 4, 5, 6, 7]

# #Q1 : WAF to print the length of a list
# def print_len(list) :
#     print(len(list));

# print_len(cities);
# print_len(villages);


# #Q2 : WAF to print the elements of a list in a single line
# def print_el(list) :
#     for elem in list :
#         print(elem, end = " ");
#     else :
#         print();

# print_el(cities);
# print_el(villages);


# #Q3 : WAF to print factorial of n
# def print_fact(n) :
#     fact = 1;
#     for i in range(1 , n+1) :
#         fact *= i;
#     return fact;

# num = int(input("Enter the number: "))
# print("Factorial of", num , "is", print_fact(num));


# #Q4 : WAF to convert USD to INR
# def USD_INR(usd) :
#     return usd * 88.95

# usd = float(input("Enter the Dollar($) amount:"))
# print(usd,"$ in INR = ", USD_INR(usd), "rs");




# #Recursion.
# #When a Function calls itself.
# #Ex:
# def show(n) :
#     if(n == 0) :  # --> Base Case
#         return;
#     print(n)
#     show(n-1)   # --> Recursive call
 
# show(10);


# #Q1 : Factorial
# def factorial(n) :
#     if(n == 1 or n == 0) :
#         return 1;
#     return n * factorial(n-1);

# num = int(input("Enter the number: "))
# print("Factorial of", num , "is", factorial(num));


# #Q2 : WAF recusrsively to calculate sum of first natural numbers.
# def calSum(n) :
#     if(n == 0) :
#         return 0;
#     if(n == 1) :
#         return 1;

#     return n + calSum(n-1);

# n = int(input("Enter the number: "))
# print("Sum of first", n , "natural numbers is", calSum(n));



# #Q3 : WAF to print all elements of list using recursion
# values = ["A", "B", "C", "D", "E"]

# def printList(lst, index):
#     n = len(lst)

#     if index >= n or index < -n:
#         print("List index out of bound.")
#         return
    
#     if index < 0:
#         index = n + index   # Example: -5 → 0, -4 → 1, -1 → 4

#     if index >= n:
#         return

#     print(lst[index])
#     return printList(lst, index + 1)

# printList(values, -5)
