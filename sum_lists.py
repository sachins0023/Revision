def sum_list(l):
    total_sum = 0
    for i in l:
        total_sum += i
    return total_sum

sample_list = [1,2,3,4,5,6]
print("The sum of the entered list is", sum_list(sample_list))