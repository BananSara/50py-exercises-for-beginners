def max_in_list(num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    return largest

print(max_in_list([3,10,11,6,1,2]))
    
    