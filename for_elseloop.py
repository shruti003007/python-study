for x in range(6):
    print(x)
else:
   print("finally finished")  

for x in range (6):
    if x == 3:   break
    print(x)
  
else:
   print("finally finished")  


successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break

successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")


successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")
  


