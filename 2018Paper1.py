# Write a program that checks which numbers from a series of numbers entered by 
# the user are prime numbers.
# The program should get a number from the user and then display the messages:
# • "Not greater than 1" if the number entered is 1 or less
# • "Is prime" if the number entered is a prime number
# • "Is not prime" otherwise.
# The user should then be asked if they want to enter another number 
# and the program should repeat if they say that they do.
# A prime number is a positive integer that will leave a remainder if it is divided
# by any positive integer other than 1 and itself.
# You may assume that each number entered by the user is an integer.
# If your program only works correctly for some prime numbers you will get 
# some marks for this question. To get full marks for this question, your program must 
# work correctly for any valid integer value that the user enters.

def getPrime():
    number = int(input("Enter number: "))
    if number <= 1:
        print("Not greater than 1")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("Is not prime")
                break
        else:
            print("Is prime")
    ans = input("Would you like to enter another number? y/n ")
    if ans.lower() == "y":
        getPrime()
    else:
        print("Goodbye")
        
getPrime()