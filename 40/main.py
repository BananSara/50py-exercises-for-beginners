import random

def generate_anagram(word):
    anagram_random = random.sample(word, len(word))
    return ''.join(anagram_random)

def guess():
    words = ['blue','red','orange','violet','yellow','black','green']
    answer = random.choice(words)
    print('computer guessed a word...')
    anagram = generate_anagram(answer)
    print(f'word anagram: {anagram}')

    while True:
        user_guess = input('what is your guess: ').strip().lower()
        if user_guess == answer:
            print(f'Correct! The word was: {answer}')
            break
        else:
            print("Incorrect. Try again!")
            
guess()