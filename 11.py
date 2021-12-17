#  ააწყე კალკულატორი

def mimateba(x, y):
    return x + y

def gamokleba(x, y):
    return x - y

def gamravleba(x, y):
    x * y

def gayofa(x, y):
    x / y

print("აირჩიეთ სასურველი მოქმედება")
print("1. მიმატება ")
print("2. გამოკლება ")
print("3. გამრავლება ")
print("4. გაყოფა ")

while True:
    choice = input("აირჩიეთ 1 / 2 / 3 / 4 ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("შემოიტანეთ პირველი რიცხვი "))
        num2 = float(input("შემოიტანეთ მეორე რიცხვი "))
    if choice == '1':
        print(num1, '+', num2, '=', mimateba(num1, num2))
    if choice == '2':
        print(num1, '-', num2, '=', gamokleba(num1, num2))
    if choice == '3':
        print(num1, '*', num2, '=', gamravleba(num1, num2))
    if choice == '4':
        print(num1, '/', num2, '=', gayofa(num1, num2))
        break
    else:
        print("მოცემული ქმედება გაუგებარია")



