# map
def map_func(func,list):
    c = []
    for char in list:
        c.append(func(char))
        # max(char)
        # max(5)
    return c

# filter
def filter_func(func,list):
    c = []
    for char in list:
        if func(char) == True:
            c.append(char)
    return c

# reduce
def reduce_func(func, items, start=None):
    # Start with the first item or the given start value
    if start is None:
        result = items[0]
        items = items[1:]  # Skip the first item since we used it as the start
    else:
        result = start

    # Go through each item and apply the function
    for item in items:
        result = func(result, item)
    
    return result


print(map_func(lambda x: x**2, [1,2,-45,3,20]))
print(reduce_func(lambda x,y: x + y, [1,2,45,3,20]))



