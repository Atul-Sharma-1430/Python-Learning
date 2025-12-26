# #List in Python == Similar To arrays in Other languages.

# # A list is a built-in Data type that Stores set of values.
# # It can Store elements of ""Different Data types"" together Unlike Arrays


# #Examaples
# marks = [87, 54, 93, 89, 76,];
# print(marks);

# student = ["Atul", "Comp", 42, "C", "Mumbai"];
# student[0] = "Aditya" # --> This is allowed here cz Lists are Mutable.

# print(len(student));   # --> Returns the length of the list
# print(type(marks));    # --> <class 'list'>
# print(type(student));  # --> <class 'list'>


# #Slicing --> All rules are same as String it gives SubList.
# #Negative Indexing --> All same as Strings.


# #List Methods (imps). Make changes in original list
# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 5];
# charList = ['a', 'c', 'd', 'e', 'f', 'h', 'b'];
# print(numList);
# print(charList);
# print("\n");

# numList.append(11); # --> Add the element at the end of the list.
# charList.append('i');
# print(numList);
# print(charList);
# print("\n");

# numList.sort();  # --> Sorts in Ascending order
# charList.sort(); # --> Sorts in Ascending order based on characters 
# print(numList);
# print(charList);
# print("\n");

# numList.sort(reverse = True);  # --> Sorts in Descending Order
# charList.sort(reverse = True); # --> Sorts in Descending order based on characters
# print(numList);
# print(charList);
# print("\n");

# numList.reverse(); #--> Reverses the List and returns none
# print(numList);
# print("\n");

# numList.insert(2 , 12); # --> Adds the elemens at given index.
# charList.insert(1 , 'b');
# print(numList);
# print(charList);
# print("\n");

# numList.remove(12); #--> removes first occurance of the element and returns it. None if not exists
# charList.remove('b');
# print(numList);
# print(charList);
# print("\n");

# numList.pop(0); # --> Removes element at that index and returns the number. None if not exists
# charList.pop(0);
# print(numList);
# print(charList);
# print("\n");

# print(numList.count(4)); # --> Counts the number of Occurance.

# list2 = numList.copy(); # --> return the copy of the List
# print(list2);



#*********************************************************************************#



# #Tuples.
# #A tuple is a built-in Data type that lets us to create ""immutable sequences"" of values.

# #Different methods to Create a Tuple
# tup0 = (); # --> Empty Tuple
# tup1 = (23, 24, 35, 78,);
# tup2 = (15,); # --> Here comma is very important to shows that it is a Tuple else it is considered as normal number
# tup3 = (1,2,3);
# tup4 = ("Atul Sharma");
# tup5 = ("Atul", 42);
# print(tup0, type(tup0));
# print(tup2, type(tup2));
# print(tup5, type(tup5));


# #Slicing --> Same as List


# #Tuple Methods.
# tup = (81,32,13,42,50,68,50,81,81,32,13,42,50,68,50,81,);
# print(tup.index(50)); # --> Returns the index of first occurance, (4) here.
# print(tup.count(81)); # --> Count total Occurance


# #Q1: WAP to ask the user to enter the name and their favourite movies and store them in a list.
# userInfo = [];
# userInfo.append(input("Enter your name:"));
# userInfo.append(input("Enter your first favourite movie name:"));
# userInfo.append(input("Enter your second favourite movie name:"));
# userInfo.append(input("Enter your third favourite movie name:"));
# print(userInfo);



# #Q2: WAP to check if a list contains a palindrome of elements.
# #Method 1
# List = [1,2,3,4,5,4,3,2,1];
# orgList = List.copy();
# orgList.reverse();
# if(orgList == List):
#     print("Pallindrome.");
# else:
#     print("Not Pallindrome.")

# #Method 2
# lst = ['a', 'b', 'c', 'z', 'a'];
# if lst == lst[::-1]:   # --> lst[::-1] → reverses the list
#                        # == → checks if the reversed list is the same as the original
#                        # lst[start : end : step] — This is called slicing
#                        # so semicolons measn start from start to end and -1 means move backwards.

#     print("Pallindrome.");
# else:
#     print("Not Palindrome.");



# #Q3:WAP to count the number of students with "A" grade in the following tuple
# grades = ('A', 'B', 'C', 'D', 'A', 'A', 'A');
# print("The number of Students who has got A grade is", grades.count('A'));
# grade = ['A', 'B', 'C', 'D', 'A', 'G', 'A'];
# grade.sort()
# print(grade);
# print(grade.sort()); # --> Gives NONE as sorting returns nothing.


