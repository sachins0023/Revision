def sum_squares(num):
    sum_value = 0
    for i in range(1,num+1):
        sum_value += i**2
    return sum_value

number = int(input("Enter the number: "))
print(f"The sum of squares of first {number} natural numbers is", sum_squares(number))