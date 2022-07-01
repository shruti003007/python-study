#simple for loop
fruit = ["apple", "banana", "orange"]
for x in fruit:
    print(x)

# looping through string
for x in "banana":
    print(x)

for number in range (3):
    print("attempt")
    print("attempt" , number)
    print("attemt" , number + 1)
    print("attempt" , number + 1, (number + 1) * ".")

for number in range(1,4):
    print("attempt", number , number * " . ") 

for number in range(1, 10, 2):
    print("attempt" , number , number * " . ")