
""" bill = int(input("enter your bill :"))
print(bill)
x = input("do you want to tip? Yes or No: ")
if x == "yes":
    tipPercentageRaw = int(input("enter your tip percentage: "))
    tipPercentage = tipPercentageRaw / 100
    print((bill * tipPercentage) + bill)
if x == "no":
    print(bill) """






bill = int(input("enter your bill :"))
print(bill)
service = input("Was the service good? Pick 'bad', 'okay', 'good', or 'great': ")
if service == "bad":
    service = int(input(bill))
elif service == "okay":
    service = int(input((bill * (15 / 100)) + bill))
elif service == "good":
    service = int(input((bill * (20 / 100)) + bill))
elif service == "great":
    service = int(input((bill * (25 / 100)) + bill))

