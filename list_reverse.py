def list_reverse(l):
    new_list = []
    for i in range(len(l)-1,0,-1):
        new_list.append(l[i])
    new_list.append(l[0])
    return new_list

sample_list = [1,2,5,6,3,2,8]
print("The reversed list is", list_reverse(sample_list))