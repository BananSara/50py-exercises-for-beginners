def generate_n_chars(integer,character):
    c = []
    for i in range (integer):
        c.append(character)
    return ''.join(c)
    
print(generate_n_chars(4,'s'))