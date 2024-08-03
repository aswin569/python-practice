import random
import math

lower = int(input("Enter the starting range :"))
upper = int(input("Enter the final range :"))

x = random.randint( lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))

print("/n\t You have only", total_chances,"to guess the number")

count =0
flag = False

while count < total_chances:
    count = count +1

    guess = int(input("Enter the guess :"))

    if guess == x:
        print("Congragulations!!!, You gussed right")
        flag = True
    elif guess < x:
        print("You gussed too small")
    elif guess > x:
        print("You gussed too large")

if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")