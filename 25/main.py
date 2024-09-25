def make_ing_form(word):
    # for char in word:
    if word.endswith('ie'):
        return word[:-2] + 'y' + 'ing'

    elif word.endswith('e'):
        if word.endswith('ee'):
            return word + 'ing'
        elif word.endswith('e'):
            if word.endswith('ee'):
                return word + 'ing'
            else:
                return word[:-1] + 'ing'

    elif (len(word) >= 3 and word[-1] not in 'aeiou' and word[-2] in 'aeiou' and word[-3] not in 'aeiou'):
        return word + word[-1] + 'ing'
    
    else:
        return word + 'ing'

print(make_ing_form('hug'))