import string 

def check_alphabets(text):
    alphabets = set(string.ascii_lowercase)
    text = set(text.lower())
    if alphabets.issubset(text):
        return True
    else:
        return False

print(check_alphabets('The quick brown fox jumps over the lazy dog'))
