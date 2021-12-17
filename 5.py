#  Write a program to accept a number from a user
#  and calculate the sum of all numbers from 1 to a given number

def mtvleli(x):
    user = int(input("type your number: "))
    sum = 0

    for i in range(1, user + 1):
        sum = sum + i
    return sum

print(mtvleli(10))

