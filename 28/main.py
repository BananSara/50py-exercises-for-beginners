def find_longest_word(words):
    map_len = map(len,word_list)
    len_word = list(map_len)
    largest_len = max(len_word)
    
    return largest_len


word_list = ['apple','chair','banana','sun','blueberry']
print(find_longest_word(word_list))

