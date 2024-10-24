def word_length():
    file_input = input('enter your file: ')
    file = open(file_input, 'r')
    words = file.read().split()
    total_words = len(words)
    
    count = 0
    for word in words:
        count += len(word)
    avg_length = count / total_words
    return avg_length

print(word_length())