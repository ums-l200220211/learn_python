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



