num = int(input("Enter a number :"))
flag = False
if num == 1:
    print("It is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print("It is not a prime  number")
else:
    print("It is a prime number")




