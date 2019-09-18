def elements_in_odd(l):
    odd_list = []
    for i in range(len(l)):
        if i%2 == 1:
            odd_list.append(l[i])
    return odd_list

sample_list = [1,2,3,4,5,6]
print("The elements in odd positions of the list is", elements_in_odd(sample_list))