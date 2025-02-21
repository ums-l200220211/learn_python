# nama = 'Naufal'
# nim = 'l200220211'
# prodi = 'teknik informatika'

# mhs = "ada seorang mahasigma yang bernama " + nama + " dengan NIM " + nim + " yang sedang menempuh pendidikan di prodi " + prodi
# print(mhs)

# nama = 'Maulana '
# print(nama*3)

# dzikir = 'subhanalah Walhamdulillah wala ilAha illallah wallahuakbar'
# print(dzikir.count('la'))

# print(dzikir.replace('la', 'LA'))

# print(dzikir.upper())

# print(dzikir.lower())

# print(dzikir.capitalize())

# print(dzikir.title())

# print(dzikir.swapcase()) #kebalikannya


# #function and getting help
# help(round)
# help(round(-2.01))
# help(print)


# studi python with W3School
print("Hello, World!")
#cek versi python
import sys
print(sys.version)
# indentasi
if 5 > 2 :
    print("Five is greater than two!") #menjorok
if 5 > 2 :
        print("Five is greater than two!") # lebih menjorok
            #    print("Five is greater than two!") #error
               
# Variabel
x = 2
x = "sally"
X = 3 # X and x are different variables
y = "Hello, World!"
print(x)
print(y)

# Comments(this is a comment)
"""
This is a comment
written in
more than just one line
"""

# variable casting(specify a variable data type)
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(f"x = {x}, y = {y}, z = {z}") # f-string
print(type(x), type(y), type(z)) 

"""Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

# Legal Variabel Name
myvar = "zul"
my_var = "zul"
_my_var = "zul"
myVar = "zul"
MYVAR = "zul"
myvar2 = "zul"

print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

# Illegal Variabel Name
# 2myvar = "zul" #number
# my-var = "zul" #minus
# my var = "zul" #space

# Camel Case
myVariableName = "Zul"
# Pascal Case
MyVariableName = "Zul"
# Snake Case
my_variable_name = "Zul"
print(myVariableName, MyVariableName, my_variable_name)

# Many Values to Multiple Variables
buah, warna, harga = "jeruk", "Orange", 2000
print(buah, warna, harga)

# One Value to Multiple Variables
buah = sayur = tanaman = "Tomat"
print(buah, sayur, tanaman)

# Unpack a List
workOut = ["push up", "pull up", "sit up"]
Chestday, Backday, Absday = workOut
print("list = ",Chestday, Backday, Absday)
# Unpack a Tuple
WorkOut = ("Push up", "Pull up", "Sit up")
Chestday, Backday, Absday = WorkOut
print("tuple = ",Chestday, Backday, Absday)
# Unpack a String
WorkOut = "Push up, Pull up, Sit up"
(Chestday, Backday, Absday) = WorkOut.split(", ") #split string
print("string = ",Chestday, Backday, Absday)

# Global Variables and Local Variables
barbel = "20kg"
def bebanBarbel():
    Barbel = "10kg" #local variable
    
    global barbel
    barbel = "30kg" #global variable (change the value of a global variable inside a function)
    
    print(f"I am doing chest day with {Barbel} and {barbel}" ) 
bebanBarbel()
print(f"I am doing chest day with {barbel}") #global variable

x = 4 
cmplx = complex(x) #complex number
print(type(cmplx)) 
# print(len(cmplx)) #error 

# Data Type in Python
x = "Hello, World!" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple
x = range(6) #range
x = {"name" : "John", "age" : 36} #dict
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
x = None #None
print(type(x))

# random number
import random
print(random.randrange(1, 10)) #random number between 1 to 9 

# string in python
x = "Hello, World!" #double quotes
x = 'Hello, World!' #single quotes
x = 'Hello, "World!"' #single quotes inside double quotes 
print(x)  

# string as array
x = "Hello, World!"
print(x[1]) #e
print(x[2:5]) #llo
print(x[-5:-2]) #orl
print(len(x)) #12

# loop through a string
for i in "Barbel":
    print(i)

# check string
txt = "Chesday is the best day"
if "Ches" in txt:
    print("Yes, 'Ches' in txt")

# check if not
txt = "Chesday is the best day"
if "leg" not in txt:
    print("Yes, 'leg' not in txt")

# format string
x = 4
txt = f"my age is {x+16} and my GPA is {x:.2f}" 
print(txt)

# escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# \'    Single Quote
# \\    Backslash
# \n    New Line
# \r    Carriage Return
# \t    Tab
# \b    Backspace
# \f    Form Feed
# \ooo  Octal value
# \xhh  Hex value
print("Hello\nWorld!") #new line
print("Hello\tWorld!") #tab   

# string method
a = " Hello, World! "
print(a.translate({119: 101, 111: 105, 114: 117})) #translate
print(a.strip()) #remove whitespace from beginning or end
print(a.lstrip()) #remove whitespace from beginning
print(a.rstrip()) #remove whitespace from end
# masih banyak method lainnya

# Boolean Values
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

x = 200
print(isinstance(x, int)) #check if x is an integer

def fungsiBool():
    return True
if fungsiBool():
    print("Yes")
else:
    print("No")

# Python Operators
# Arithmetic Operators
x = 5
y = 3
print(x + y) #8
print(x - y) #2
print(x * y) #15
print(x / y) #1.6666666666666667
print(x % y) #2
print(x ** y) #125
print(x // y) #1
print(100 + 5 * 3) #115 (5 * 3 = 15, 100 + 15 = 115)

# Assignment Operators
x = 5
x += 3
print(x) #8
x -= 3
print(x) #5
x *= 3
print(x) #15
x /= 3
print(x) #5.0
x %= 3
print(x) #2.0
x **= 3
print(x) #8.0
x //= 3
print(x) #2.0

# Comparison Operators
x = 5
y = 3
print(x == y) #False
print(x != y) #True
print(x > y) #True
print(x < y) #False
print(x >= y) #True
print(x <= y) #False

# Logical Operators
x = 5
print(x > 3 and x < 10) #True
print(x > 3 or x < 4) #True
print(not(x > 3 and x < 10)) #False

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #True
print(x is y) #False
print(x == y) #True

# Membership Operators
x = ["apple", "banana"]
print("banana" in x) #True
print("pineapple" not in x) #True

# Bitwise Operators
x = 5
y = 3
print(x & y) #1
print(x | y) #7
print(x ^ y) #6
print(~x) #-6
print(x << 2) #20
print(x >> 2) #1

# Python Collections (Arrays)
# List
listAlatGym = ["Barbel", "Dumbell", "Pull up bar"]
print(listAlatGym)

# Access Items
print(listAlatGym[1]) #Dumbell
print(listAlatGym[-1]) #Pull up bar
print(listAlatGym[1:2]) #['Dumbell']
print(listAlatGym[:2]) #['Barbel', 'Dumbell']
print(listAlatGym[1:]) #['Dumbell', 'Pull up bar']

# Change Item Value
listAlatGym[1] = "Kettlebell"
print(listAlatGym)

# insert() method
listAlatGym.insert(2, "Dumbell")
print(listAlatGym)

# append() method
listAlatGym.append("Bench press")
print(listAlatGym)

# extend() method
listAlatGym.extend(["Squat rack", "Treadmill"])
print(listAlatGym)

# remove() method
listAlatGym.remove("Treadmill")
print(listAlatGym)
# pop() method
listAlatGym.pop(1) #remove index 1
print(listAlatGym)
# del keyword
del listAlatGym[2] #remove index 2
print(listAlatGym)
# clear() method
listAlatGym.clear() #remove all items
print(listAlatGym)

# loop through a list
listAlatGym = ["Barbel", "Dumbell", "Pull up bar"]
for i in listAlatGym:
    print(i)

# Loop Through the Index Numbers
for i in range(len(listAlatGym)): #range(3) = 0, 1, 2
    print(listAlatGym[i])   

# Using a While Loop
i = 0 #index
while i < len(listAlatGym): #range(3) = 0, 1, 2
    print(listAlatGym[i]) 
    i += 1 #increment the index
    
# List Comprehension
[print(i) for i in listAlatGym]

# example List Comprehension
newListAlatGym = [] #empty list
for i in listAlatGym: #loop through listAlatGym
    if "e" in i: #check if 'a' in i
        newListAlatGym.append(i) #add i to newListAlatGym
print(newListAlatGym) #['Barbel', 'Dumbell', 'Pull up bar']

# Example List Comprehension
newListAlatGym = [i for i in listAlatGym if "e" in i] #loop through listAlatGym and add i to newListAlatGym if 'e' in i
print(newListAlatGym) #['Barbel', 'Dumbell', 'Pull up bar']

# Example List Comprehension
listAlatGym = ["Barbel", "Dumbell", "Pull up bar"]
newListAlatGym = ["Pull up bar" for i in listAlatGym] #loop through listAlatGym and add 'Pull up bar' to newListAlatGym
print(newListAlatGym) #['Pull up bar', 'Pull up bar', 'Pull up bar']

# Example List Comprehension
newListAlatGym = [i if i != "Barbel" else "Treadmill" for i in listAlatGym] #loop through listAlatGym and add i to newListAlatGym if i != 'Barbel' else add 'Treadmill'
print(newListAlatGym) # ['Treadmill', 'Dumbell', 'Pull up bar']

# Sort List Alphabetic
listAlatGym.sort()
print(listAlatGym)

# Sort List Numerically
ListBeban = [20, 10, 30, 5]
ListBeban.sort()
print(ListBeban)

# Sort Descending
ListBeban.sort(reverse = True)
print(ListBeban)

# Custom Sort Function
def myfunc(n): 
  return abs(n - 82) #return the absolute value of n - 82
thislist = [100, 50, 65, 82, 23] 
thislist.sort(key = myfunc) #sort the list based on the return value of the function
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #sort the list based on the lower case
print(thislist)

# Reverse Order
thislist.reverse()
print(thislist)

# Copy a List
newListAlatGym = listAlatGym.copy()
print(newListAlatGym)
# Another way to make a copy is to use the built-in method list()
newListAlatGym = list(listAlatGym) 
print(newListAlatGym)
# Another way to make a copy is to use the slice operator
newListAlatGym = listAlatGym[:] #listAlatGym[start:stop]
print(newListAlatGym)

# Join Two Lists
listAlatGym = ["Barbel", "Dumbell", "Pull up bar"]
ListBeban = [20, 10, 30, 5]
listGabungan = listAlatGym + ListBeban
print(listGabungan)

# Append List
for i in ListBeban:
    listAlatGym.append(i)
print(listAlatGym)

# Extend List
listAlatGym.extend(ListBeban) 
print(listAlatGym) 

# Tuple (ordered and unchangeable)
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown")
print(tupleAlatGym)

# Access Tuple Items
print(tupleAlatGym[1]) #Bench Press
print(tupleAlatGym[-1]) #Lat Pulldown
print(tupleAlatGym[1:2]) #('Bench Press',)
print(tupleAlatGym[:2]) #('Switch Machine', 'Bench Press')
print(tupleAlatGym[1:]) #('Bench Press', 'Lat Pulldown')

# Change Tuple Values
# tupleAlatGym[1] = "Kettlebell" #error
# Convert the tuple into a list, change the list, and convert the list back into a tuple    
listAlatGym = list(tupleAlatGym)
listAlatGym[1] = "Kettlebell"
tupleAlatGym = tuple(listAlatGym)
print(tupleAlatGym)

# Tuple() Constructor
tupleAlatGym = tuple(("Switch Machine", "Bench Press", "Lat Pulldown"))
print(tupleAlatGym)

# Unpack Tuples
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown")
(Switch, Bench, Lat) = tupleAlatGym
print(Switch, Bench, Lat)

# Using Asterisk*
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown", "Kettlebell")
(Switch, Bench, *Lat) = tupleAlatGym
print(Switch, Bench, Lat)
# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown", "Kettlebell")
(Switch, *Bench, Lat) = tupleAlatGym
print(Switch, Bench, Lat)

# Loop Through a Tuple
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown")
for i in tupleAlatGym:
    print(i)

# Loop Through the Index Numbers
for i in range(len(tupleAlatGym)): #range(3) = 0, 1, 2
    print(tupleAlatGym[i])

# Using a While Loop   
i = 0 #index
while i < len(tupleAlatGym): #range(3) = 0, 1, 2
    print(tupleAlatGym[i])
    i += 1 #increment the index

# Tuple Comprehension
[print(i) for i in tupleAlatGym]

# join two tuples
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown")
tupleBeban = (20, 10, 30, 5)
tupleGabungan = tupleAlatGym + tupleBeban
print(tupleGabungan)

# The tuple() Constructor
tupleAlatGym = tuple(("Switch Machine", "Bench Press", "Lat Pulldown"))
print(tupleAlatGym)

# Tuple Methods
# count() method
tupleAlatGym = ("Switch Machine", "Bench Press", "Lat Pulldown")
print(tupleAlatGym.count("Bench Press")) #1
# index() method
print(tupleAlatGym.index("Bench Press")) #1

# Set (unordered and unindexed)
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
print(setAlatGym)

# Access Items
# print(setAlatGym[1]) #error
for i in setAlatGym:
    print(i)
    
# Change Items
# setAlatGym[1] = "Kettlebell" #error
setAlatGym.add("Kettlebell")
print(setAlatGym) #{'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell'}

# Add Items
setAlatGym.add("Bench press")
print(setAlatGym) #{'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press'}

# add any iterable
listAlatGym = ["Squat rack", "Treadmill"]
setAlatGym.update(listAlatGym)
print(setAlatGym) #{'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press', 'Squat rack', 'Treadmill'}

# update() method
setAlatGym.update(["Squat rack",0])
print(setAlatGym) #{0, 'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press', 'Squat rack'}

# Get the Length of a Set
print(len(setAlatGym)) #7

# Remove Item
setAlatGym.remove("Squat rack")
print(setAlatGym) #{0, 'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press'}

# discard() method
setAlatGym.discard(0)
print(setAlatGym) #{'Barbel', 'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press'}

# pop() method
setAlatGym.pop()
print(setAlatGym) #{'Dumbell', 'Pull up bar', 'Kettlebell', 'Bench press'}

# clear() method
setAlatGym.clear()
print(setAlatGym) #set()

# del keyword
del setAlatGym
# print(setAlatGym) #error

# Loop Through a Set
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
for i in setAlatGym:
    print(i) #
    
# Check if Item Exists
print("Barbel" in setAlatGym) #True

# Join Two Sets
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {20, 10, 30, 5}
setGabungan = setAlatGym.union(setBeban)
print(setGabungan) #{'Barbel', 5, 'Dumbell', 10, 'Pull up bar', 20, 30}

# The set() Constructor
setAlatGym = set(("Barbel", "Dumbell", "Pull up bar"))
print(setAlatGym) #{'Barbel', 'Dumbell', 'Pull up bar'}

# join set
# update() method
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {20, 10, 30, 5}
setAlatGym.update(setBeban)
print(setAlatGym) #{'Barbel', 5, 'Dumbell', 10, 'Pull up bar', 20, 30}

# Union() method
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {20, 10, 30, 5}
setGabungan = setAlatGym.union(setBeban)
print(setGabungan) #{'Barbel', 5, 'Dumbell', 10, 'Pull up bar', 20, 30}

# intersection() method
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {"Barbel", 10, 30, 5}
setGabungan = setAlatGym.intersection(setBeban)
print(setGabungan) #{'Barbel'} keep only the duplicates

# difference() method
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {"Barbel", 10, 30, 5}
setGabungan = setAlatGym.difference(setBeban)
print(setGabungan) #{'Dumbell', 'Pull up bar'} keep only the differences

# symmetric_difference() method
setAlatGym = {"Barbel", "Dumbell", "Pull up bar"}
setBeban = {"Barbel", 10, 30, 5}
setGabungan = setAlatGym.symmetric_difference(setBeban)
print(setGabungan) #{'Dumbell', 5, 10, 'Pull up bar', 30} keep all but not the duplicates

# Set Methods
thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset) #False

# Dictionary (unordered, changeable and indexed)
dictAlatGym = {
    "Barbel": 20,
    "Dumbell": 10,
    "Pull up bar": 30
}
print(dictAlatGym)

# Dictionary Items
print(dictAlatGym["Barbel"]) #20
print(dictAlatGym.get("Dumbell")) #10
print(dictAlatGym.keys()) #dict_keys(['Barbel', 'Dumbell', 'Pull up bar'])
print(dictAlatGym.values()) #dict_values([20, 10, 30])
print(dictAlatGym.items()) #dict_items([('Barbel', 20), ('Dumbell', 10), ('Pull up bar', 30])

# dict() Constructor
dictAlatGym = dict(Barbel=20, Dumbell=10, Pullupbar=30)
print(dictAlatGym) #{'Barbel': 20, 'Dumbell': 10, 'Pullupbar': 30}

# del keyword
del dictAlatGym["Barbel"]
print(dictAlatGym) #{'Dumbell': 10, 'Pull up bar': 30}

# pop() method
dictAlatGym.pop("Dumbell")
print(dictAlatGym) #{'Pull up bar': 30}

# popitem() method
dictAlatGym.popitem()
print(dictAlatGym) #{}

# clear() method
dictAlatGym.clear()
print(dictAlatGym) #{}


# access items
dictAlatGym = {
    "Barbel": 20,
    "Dumbell": 10,
    "Pull up bar": 30
}
for i in dictAlatGym:
    print(i) #Barbel Dumbell Pull up bar
for i in dictAlatGym:
    print(dictAlatGym[i]) #20 10 30
for i in dictAlatGym.values():
    print(i) #20 10 30
for i in dictAlatGym.keys():
    print(i) #Barbel Dumbell Pull up bar
for i, j in dictAlatGym.items():
    print(i, j) #Barbel 20 Dumbell 10 Pull up bar 30
    
# add new item to dictionary
dictAlatGym["Kettlebell"] = 15
print(dictAlatGym) #{'Barbel': 20, 'Dumbell': 10, 'Pull up bar': 30, 'Kettlebell': 15}

# update() method
dictAlatGym.update({"Bench press": 25})
print(dictAlatGym) #{'Barbel': 20, 'Dumbell': 10, 'Pull up bar': 30, 'Kettlebell': 15, 'Bench press': 25}

# Nested Dictionaries
dictAlatGym = {
    "Barbel": {
        "Beban": 20,
        "Jumlah": 2
    },
    "Dumbell": {
        "Beban": 10,
        "Jumlah": 4
    },
    "Pull up bar": {
        "Beban": 30,
        "Jumlah": 1
    }
}
print(dictAlatGym)

# check if key exists
print("Barbel" in dictAlatGym) #True
# 
if "Dumbell" in dictAlatGym:
    print("Yes, 'Dumbell' in dictAlatGym") #Yes, 'Dumbell' in dictAlatGym   
  
# Loop Through a Dictionary
for i in dictAlatGym:
    print(i) #Barbel Dumbell Pull up bar
for i in dictAlatGym:
    print(dictAlatGym[i]) #{'Beban': 20, 'Jumlah': 2} {'Beban': 10, 'Jumlah': 4} {'Beban': 30, 'Jumlah': 1}
for i in dictAlatGym.values():
    print(i) #{'Beban': 20, 'Jumlah': 2} {'Beban': 10, 'Jumlah': 4} {'Beban': 30, 'Jumlah': 1}
for i in dictAlatGym.keys():
    print(i) #Barbel Dumbell Pull up bar
for i, j in dictAlatGym.items():
    print(i, j) #Barbel {'Beban': 20, 'Jumlah': 2} Dumbell {'Beban': 10, 'Jumlah': 4} Pull up bar {'Beban': 30, 'Jumlah': 1}
    
# copy a dictionary
newDictAlatGym = dictAlatGym.copy()
print(newDictAlatGym) #{'Barbel': {'Beban': 20, 'Jumlah': 2}, 'Dumbell': {'Beban': 10, 'Jumlah': 4}, 'Pull up bar': {'Beban': 30, 'Jumlah': 1}}

# dict() Constructor
newDictAlatGym = dict(dictAlatGym)
print(newDictAlatGym) #{'Barbel': {'Beban': 20, 'Jumlah': 2}, 'Dumbell': {'Beban': 10, 'Jumlah': 4}, 'Pull up bar': {'Beban': 30, 'Jumlah': 1}}

# Nested tree Dictionaries 
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

a = {'name': 'John', 'age': 36, 'country': 'Norway'}
b = {'name': 'mandy', 'age': 24, 'country': 'Indonesia'}
c = {'name': 'mike', 'age': 30, 'country': 'USA'}
myfamily = {'child1': a, 'child2': b, 'child3': c}
print(myfamily)

# Access Items in Nested Dictionaries
print(myfamily["child1"]["name"]) #Emil
print(myfamily["child2"]["age"]) #24
print(myfamily["child3"]["name"]) #Linus

# Python Conditions and If statements logical operators
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
# elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

# one line if else statement, with 3 conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
if a > b or a > c:
    print("At least one of the conditions is True")

# Not
if not a > b:
    print("a is not greater than b")

# Nested If
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
a = 33
b = 200
if b > a:
    pass #empty block of code that does nothing 
    
    
