
def lingo(hidden_word):
        print("Guess the 5-letter hidden word!")
        while True:
                guess = input("Enter your guess: ").lower()
                if len(guess) != 5:
                        print("Please enter a 5-letter word.")
                        continue
                
                clue = ''
                for i in range(5):
                        if guess[i] == hidden_word[i]:      # Correct letter in the correct position
                                clue += f'[{guess[i]}]'
                        elif guess[i] in hidden_word:       # Correct letter, wrong position
                                clue += f"({guess[i]})"
                        else:                               # Incorrect letter
                                clue += guess[i]
                print("Clue:", clue)          
                
                
                if guess == hidden_word:
                        print(f"You guessed it! The correct word is {hidden_word}")
                        break
                
lingo('tiger')