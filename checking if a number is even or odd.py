# PROGRAM TO TELL WHETHER A NUMBER IS EVEN OR ODD
num = int(input("Please type the number you wish to check to see if it is even or odd: "))

# inserting an if else statement and checking if the number gives a remainder when divided by 2
if (num % 2 == 0):
    print("Your number is an even number")
else:
    print("Your number is an odd number")