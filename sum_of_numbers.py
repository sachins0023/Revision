def sum_of_nums(num):
    sum_value = 0
    for i in range(1,num+1):
        sum_value += i
    return sum_value

number = int(input("Enter the number = "))
print(f"The sum of natural numbers till {number} is", sum_of_nums(number))