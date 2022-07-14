#defining function
from ast import increment_lineno


def greet():
    print("hi there")
    print("welcome abroad")


greet()

print("!!!!!!!!!!!!!!!!!!!!!")

#arguments 
def greet(first_name, last_name):
    print(f"hi {first_name}{last_name}")
    print("welcome aboard")


greet("shruti" , "kushwaha")
#greet("shruti") will display error due to missing 2nd argument

def greet (name):
    print(f"hi {name}")


greet("mosh")
print(greet("mosh"))  #o/p=>hi mosh   none in which none is the return value of greet function

print("@@@@@@@@@@@@@@@@@@@@@")

#keyword argument
def increase(number, by):
    return number + by

result = increase(2,1)
print(result)

def increase(number, by):
    return number + by

print(increase(2,1))
print(increase(2, by = 1))  #by = 1 is a keyword argument

print("############")

#default arguments
def increament(number, by = 1):
    return number + by

print(increament(2))  #by default it will take 1 coz of missing 1 argument
print(increament(2,5)) #both arguments are giver so will print 7

print("%%%%%%%%%%%%%%%%")

#xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
       # total = total * number
        total *= number
    return total
print(multiply(2,3,4,5))

#basics in xargs
def multiply(x,y):
    return x * y

print(multiply(2,3))
#multiply(2,3,4,5) will not work 

def multiply (*numbers):
    for number in numbers:
        print(number)

print(multiply(2,3,4,5))

print("^^^^^^^^^^^^^^^^^")

#xxargs(**args)

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save_user( id = 1, name = "shruti", age = 22)

