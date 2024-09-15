# nums = input('Please enter an array of your numbers, separated by spaces: ')
# nums = [int(i) for i in nums.split()]

def sum(x):
    c = 0
    for i in x:
        c += i 
    print(f'sum: {c}')

sum([1,2,3,4])


def multiply(y):
    c2 = 1
    for i in y:
        c2 *= i
    print(f'multiply: {c2}')
    
multiply([1,2,3,4])


