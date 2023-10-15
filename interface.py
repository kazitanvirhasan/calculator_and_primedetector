# python calculator app


# functions decleretion

def add(num1, num2):
    result = num1 + num2
    print("{0}+{1}={2}".format(num1,num2,result))


def sub(num1, num2):
    result = num1 - num2
    print("{0}-{1}={2}".format(num1,num2,result))



def multi(num1, num2):
    result = num1 * num2
    print("{0}*{1}={2}".format(num1,num2,result))


def devide(num1, num2):
    result = num1 / num2
    print("{0}/{1}={2}".format(num1,num2,result))

print ("this is a simple python calculator ")
print("what do you ant to do ??")

print("1 for add")

print("2 for sub")

print("3 for multi")

print("4 for divide")

# user input


choise = input(" enter a choise : ")

num1 = float(input("enter num 1 : "))

num2 = float(input("neter num 2 : "))

# if statments
if choise == "1":
    add(num1, num2)

elif choise == "2":
    sub(num1, num2)

elif choise == "3":
    multi(num1, num2)

elif choise == "4":
    devide(num1, num2)

else:
    print(" please select a valid choise")