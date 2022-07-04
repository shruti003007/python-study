i = 1
while i < 6:
    print(i)
    i += 1

#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

number = 100
while number > 0:
    print(number)
    number //= 2

#taking input from terminal
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

#case sesitive so input can be in any case
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)

#better line. line 33 will change input into lowercase and then will comare it with quit  
command = ""
while command.lower() != "quit":
    command = input (">")
    print("ECHO", command)

#infinte loop
#while True:
#    command = input(">")
#   print("ECHO", command)
#   if command.lower() == "quit"
   # break
