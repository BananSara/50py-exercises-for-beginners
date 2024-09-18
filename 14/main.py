def words_to_lengths(words):
    c = []
    for i in words:
        c.append(len(i))
    return c


word = ['apple', 'banana', 'cherry', 'date']
print(words_to_lengths(word))
