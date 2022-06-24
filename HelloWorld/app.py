print("Hello World")
print("*"*10)
print("Hello Juhi")
print("Hello sweetu")
# 2+
# print"Helloworld"
#x = 1
# strings
course = "python programming"
print(len(course))
print(course[0])  # display 1st alphabet
print(course[-1])  # display last alphabet
print(course[0:3])  # last 3rd alphabet will not be included
print(course[:3])  # diplay 0-2 index in string
print(course[0:])  # 0-all index
print(course[:])  # display whole string
# escape sequenses
course1 = "python \"programming"  # \indicate escape sequence
course2 = "python \'programming"
course3 = "python \\programming"
course4 = "python \nprogramming"
print(course1)
print(course2)
print(course3)
print(course4)
# formatting string
first = "juhi"
last = "kushwaha"
full1 = first + " " + last  # old method
full2 = f"{first} {last}"  # new method
full3 = f"{len(first)} {last}"
full4 = f"{len(first)} {2+2}"
print(full1)
print(full2)
print(full3)
print(full4)
# string method
course = "python programming"
# will not effect original string and will display all in upper case
print(course.upper())
print(course.lower())  # all alphabet will display in lower case
print(course.title())  # 1st alphabet of string will disply in capital form
print(course)
