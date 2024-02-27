

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




""" print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
calculate = int(input("Choose your operation:" ))

if(calculate in [1,2,3,4]):
    if (calculate == 1):
        x = float(input("Please enter your first number:" ))
        y = float(input("Please enter your second number:" ))
        print("The answer is: " + str(x + y))
    elif (calculate == 2):
        x = float(input("Please enter your first number:" ))
        y = float(input("Please enter your second number:" ))
        print("The answer is: " + str(x - y))
    elif (calculate == 3):
        x = float(input("Please enter your first number:" ))
        y = float(input("Please enter your second number:" ))
        print("The answer is: " + str(x * y))
    elif (calculate == 4):
        x = int(input("Please enter your first number:" ))
        y = int(input("Please enter your second number:" ))
        print("The answer is: " + str(x / y))

else:
    print("Invalid operation") """





""" number = int(input("Enter number to find factors: "))

print("Factors of number {} are : ".format(number))
for i in range(1, number + 1):
    if(number % i == 0):
        print(i) """




""" num1 = int(input("Enter first number for gcf: "))
num2 = int(input("Enter second number: "))


def factor1():
    for i in range(1, num1 + 1):
        if(num1 % i == 0):
            factor1.append(i)


def factor2():
    for i in range(1, num2 + 1):
        if(num2 % i == 0):
            factor2.append(i)

def cf():
    for i in factor1:
        if i == i in factor2:
            print(cf)

print(cf) """


num1 = int(input("Enter first number for gcf: "))
num2 = int(input("Enter second number: "))

def Gcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
            return gcf

print("The greatest common factor is "+str(Gcf(num1, num2)))