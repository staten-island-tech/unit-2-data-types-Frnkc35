

""" x = 4
y = 4

x = input(x,y)
if (x == 4 , y == 4):
    print("yes")
else:
    print("no") """






""" x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))

def gcf(x,y):
    if x > y:
        print("testing")

gcf(x,y)
 """




""" def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("frankie", "chen")

print(full_name) """



""" number = int(input("Enter number to find factors: "))

print("Factors of number {} are : ".format(number))
for i in range(1, number + 1):
    if(number % i == 0):
        print(i) """


print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
calculate = int(input("Choose your operation:" ))

if(calculate in [1,2,3,4]):
    if (calculate == 1):
        x = int(input("Please enter your first number:" ))
        y = int(input("Please enter your second number:" ))
        print("The answer is:" + str(x + y))
    elif (calculate == 2):
        x = int(input("Please enter your first number:" ))
        y = int(input("Please enter your second number:" ))
        print("The answer is:" + str(x - y))
    elif (calculate == 3):
        x = int(input("Please enter your first number:" ))
        y = int(input("Please enter your second number:" ))
        print("The answer is:" + str(x * y))
    elif (calculate == 4):
        x = int(input("Please enter your first number:" ))
        y = int(input("Please enter your second number:" ))
        print("The answer is:" + str(x / y))

else:
    print("Invalid operation")






