def find_max(l):
    max_value = l[0]
    for i in l:
        if i>max_value:
            max_value = i
    return max_value

sample_list = [3,8,6,5,3]
print("The maximum value in your list is",find_max(sample_list))