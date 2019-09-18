def find_factorial(number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial*i
    return factorial

number = int(input("Enter your number: "))
factorial_value = find_factorial(number)
print(f"{number} ! = ", factorial_value)