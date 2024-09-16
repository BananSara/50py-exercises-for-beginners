
# user_str = input('enter your string: ')
# def reverse(string):
#     return string [::-1]    
#     # means that: sequence[start:stop:step]
    
# print(reverse(user_str))

# ======================================

def reverse(x):
    new = []                           
    for i in range(len(x))[::-1]:      
        new.append(x[i])               
    print (''.join(new))              

reverse('I am testing')