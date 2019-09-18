def isExist(element, l):
    if element in l:
        return True
    else:
        return False

sample_list = [4,5,3,8,3,4,4]
sample_element = 6
if isExist(sample_element,sample_list) == True:
    print("Your element exists in the list")
else:
    print("Your element does't exist in the list")