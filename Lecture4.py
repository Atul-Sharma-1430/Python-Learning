#Dictionaries == Similar to objects in JS.
#Dictionaries are used to store data values in ""key:value"" pairs.
#They are ""unordered, mutable"" and ""don't allow duplicates keys"".

# dict = {
#     "Key" : "Value",
#     "Name": "Atul",
#     "Standard" : "14th",
#     "Branch" :"Comps",
#     "Age" : 21,
#     "list" : [80 , 90 , 100 , 76],
#     "isPass" :True,
#     "topics" : ("Dictionaries" , "Sets"),
#     1 : "Atul",
#     2 : "Aditya",
#     3 : "Jason"
# }

# print(dict["Name"]); # --> Accessing methods number 1.
# dict["Surname"] = "Sharma"; # --> We can assign a new key value pair also in dict added at last generally
# print(dict)

# dict["list"].sort() # --> Method to sort.
# print(dict["list"]);

# dict["Name"] = "Aditya";
# print(dict["Name"]);

# print(dict[1]); # --> Atul
# print(type(dict)); # --> <class 'dict'>



# #Empty Dictionary
# emptyDict = {}
# print(emptyDict);



# #Nested Dictionary
# student = {
#     "Name" : "Atul Sharma",
#     "marks" : {
#         "Java" : 90,
#         "C" : 80,
#         "DSA" : 98
#     },
#     "Branch" : "Computer",
#     "SEM" : 3
# }
# print(student["marks"]["Java"]) # --> Accessing nested values.



#Dictionary Methods. (Commonly Used)
# sports = {
#     "Cricket" : 11,
#     "Soccer" : 22,
#     "kabaddi" : 7,
#     "Chess" : 2
# }

# print(len(sports)); # --> gives total number of key value pairs.
# print(len(list(sports.keys()))); # --> Type casting into list then finding the length

# print(sports.keys()); # --> return the set of all keys.
# print(type(sports.keys())); ## --> <class 'dict_keys'>

# print(sports.values());  # --> return the set of all values.
# print(type(sports.values())); ## --> <class 'dict_values'>

# print(sports.items()) # -->  Returns all the key value pairs as tuples
# print(type(sports.items())); # --> <class 'dict_items'>

# print(sports.get("Soccer1")); # --> Does not gives error if key not found
# print(sports["Soccer1"]); # --> gives error if key not found

# sports.update({"Ludo" : 4}); # --> Adds new key value pair.
# newDict = {"FreeFire" : 48}
# sports.update(newDict);
# print(sports);



#*********************************************************************************#



# Sets
# Set is the collection of ""unordered items""
# Each element in the set must be unique and immutable.

# nums = {1,2,3,4,5,6}
# collection = {1,2,2,2,} # --> Same as {1,2} as duplicates values are ignored
# print(nums , type(nums), len(nums)) # --> {1, 2, 3, 4, 5, 6} <class 'set'> 6
# print(collection, type(collection), len(collection)) # --> {1, 2} <class 'set'> 2


# #Empty Set
# emptySet = set() # --> Syntax to Create Empty Set.
# print(emptySet) # --> Output : set()


# Set Methods
# Set is Mutable but its elememts are immutable hence in .add() we can pass tuples but can't pass dict and list.
# fruits = {"Mango", "Banana", "Litchi", "Kiwi", "Grapes", "Pineapple"}
# values = {'a', 'b', 'c', "Grapes"}

# fruits.add("Orange") # --> Adds new element
# print(fruits)

# fruits.add(('a', 'b', 'c')) # --> This can be added as it is a Tuple
# print(fruits)

# fruits.add([1,2,3,4]) # --> This cannot be added as list are mutable n here list acts as element of set which   are immutable hence cannot be added n same for dict also
# print(fruits) # --> TypeError: unhashable type: 'list' measn ""hashvalue"" cannot be created

# fruits.remove("Orange") # --> Removes the element
# print(fruits)

# fruits.remove("Orange") # --> Gives error bcz does not exists; KeyError: 'Orange'

# fruits.clear() # --> Empties the set.

# print(fruits.pop()) # --> Removes any random value 
# print(fruits)

# newSet = fruits.union(values) # --> Combines both set in any order and return a new set
# print(newSet)

# newSet2 = fruits.intersection(values) # --> Combines common values and return a new set
# print(newSet2)



# #Q1: Store the given word meanings in Python Dictionary
# Dictionary = {
#     "Table" : "A piece of Furniture",
#     "Facts" : {
#         "Fact1" : "I am a Good Boy",
#         "Fact2" : "I am 20 years old"
#     },
#     "Figures" : {
#         1 : "Circle",
#         2 : "Square",
#         3 : "Rectangle"
#     },
#     "Cat" : " A small Aninmal"
# }
# print(Dictionary);


# #Q2: You are given a list of subjects foe students. Assume one classroom is requires for 1 Subject. 
#     # How many Classrooms are neede by all subjects
# subjects = ["Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "C", "C#", "C++"]
# print(len(subjects))
# print("The Number of Classrooms required for all subjects is:", len(set(subjects)));



# #Q3: Take marks of 3 subjects and add it to an empty dict.
# marks = {}
# hindi = input("Enter Hindi marks: ")
# marks.update({"Hindi" : hindi})

# eng = input("Enter English marks: ")
# marks.update({"English" : eng})

# maths = input("Enter Maths marks: ")
# marks.update({"Maths" : maths})

# print(marks)


# #Q4: Figure out a way to store 9 and 9.0 as Seperate values in a set.
# store = set()

# # Method 1
# store.add(9)
# store.add("9")
# print(store)

# # Method 2
# store.add(("float", 9.0))
# store.add(("int", 9))
# print(store)
