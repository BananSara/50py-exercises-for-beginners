import random

def number_guess():
    turn = 0
    computer_guess = random.randint(1,20)
    name = input('Hello! What is your name? ')
    print(f'Well, {name}, I am thinking of a number between 1 and 20. ')
    
    while True:
        user_guess = int(input('take a guess: '))
        turn += 1
        
        if user_guess == computer_guess:
            print(f'well done {name}! You guessed my number in {turn} guesses!')
            break
        elif computer_guess > user_guess:
            print('Your guess is too low. ')
        elif user_guess > computer_guess:
            print('Your guess is too high. ')
    

number_guess()
