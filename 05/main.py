vowel_chars = 'iaeou'
def translate(x):
    c = ''
    for char in x:
        if char not in vowel_chars:
            c += char + 'o' + char
        else:
            c += char
    print(c)
    
translate('this is fun')
