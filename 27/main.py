def len_list(words):
    map_words = map(len,words)
    final = list(map_words)
    return final

words = ['apple', 'orange', 'cat']
print(len_list(words))
