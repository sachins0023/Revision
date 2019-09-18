number = int(input("Enter your number: "))

def even_odd(num):
    if num%2 == 0:
        return True
    else:
        return False

if even_odd(number) == True:
    print("Number entered is even")
else:
    print("Number entered is odd")