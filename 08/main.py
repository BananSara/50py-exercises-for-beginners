user_word = input('please enter your word: ')
def palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False

print(palindrome(user_word))
    
    