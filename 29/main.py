# 1:
# def filter_long_words(words,n):
#     length = []
#     for char in words:
#         if len(char) > n:
#             length.append(char)
#     return ''.join(length)

# print(filter_long_words(['hello','cherry','abc'],4))

# ================================
# 2:
def filter_words(words,n):
    def check_len(word):
        return len(word) > n
    filter_words = filter(check_len,words)
    final = list(filter_words)
    return ' , '.join(final)


num = 4
words_list = ['hello','cherry','abc']
print(filter_words(words_list,num))



