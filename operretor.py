n = int(input("place a number hare "))
c = 1
for i in range(2,n):
    if n%2 == 0:
        c=0
if c == 1:
    print("this is a prime number")
else:
    print("this is not a prime number")