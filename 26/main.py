from functools import reduce
def compare_num(x,y):
    if x > y:
        return x
    else:
        return y

def max_in_list(num_list): 
    return reduce(compare_num, num_list)

numbers = [10,6,3,4,50,9]
print(max_in_list(numbers))


