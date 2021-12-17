# Write a program to print multiplication table of a given number

def tabula():
    user = int(input("type your number: "))
    shedegi = 0
    for i in range(1, 11):
        shedegi = i * user
    return shedegi

print(tabula())

#araa dasrulebuli