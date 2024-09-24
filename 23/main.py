import re

def correct(text):
    text =text.replace('.', '. ')
    text = re.sub(' +', ' ', text)
    return text

print(correct("This   is  very funny  and           cool.Indeed!"))