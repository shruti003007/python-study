#to print 1 to 10 
for n in range (1,11):
    print(n)

print("@@@@@@@@@@@")

#to print 10 to 1
for n in range (10,0,-1): #10 start 0 upto -1 difference of
    print(n)

print("==========")
#to print 1
       # 2 2
       # 3 3 3
for x in range (10):
    Tempstring = ""
    for y in range (x):
        # print(f"({x}, {y})")
        Tempstring = f"{Tempstring} {x} "
        # Tempstring = f"{Tempstring} * "
    print(Tempstring)

print("########")

#to print *
         # *
         # *
for n in range (1,11):
    tempstring = "*"
    print(tempstring)

print("&&&&&&&&&&&&&&&&&&&")

for x in range (10): 
    tempstring = ""
    for y in range (x):
        tempstring = f"{tempstring} * "

    print(tempstring)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
#to print *****
        # ****
        # ***
        # **
        # *
for x in range (5,0,-1):
    tempstring = ""
    for y in range (x):
        tempstring = f"{tempstring} * "
    print(tempstring)

print("****************")

#to print table 

for x in range (1,11):
    tempstring = ""
    for y in range (1, 11):
        # print(f"{x} * {y} = ",x*y)
        # print('-test-')
        tempstring = f"{tempstring} {x*y} "
    print(tempstring)
    