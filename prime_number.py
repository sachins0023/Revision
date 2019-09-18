def check_prime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            continue
    return True

number = int(input("Enter the number: "))
key = check_prime(number)
if key == True:
    print("The entered number is prime")
else:
    print("The entered number is not prime")