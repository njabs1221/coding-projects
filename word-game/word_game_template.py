def read_dictionary():

    words = []
    while True:
        line = input().upper()
        if line == '###':
            break
        words.append(line)
    return words




def compute_response(target, guess):
    
    r = ['.'] * len(guess)
    fc = [False] * len(target)

    for i in range(len(guess)):
        if i < len(target) and guess[i] == target[i]:
            r[i] = guess[i].upper()
            fc[i] = True

    for i in range(len(guess)):
        if r[i] != '.':
            continue
        for j in range(len(target)):
            if not fc[j] and guess[i] == target[j]:
                r[i] = guess[i].lower()
                fc[j] = True
                break

    return ''.join(r)            


def is_valid(guess, dictionary):
    
    return guess.upper() in dictionary


"""
DO NOT MODIFY ANY CODE BELOW THIS LINE
"""

import random

dictionary = read_dictionary()

rng = random.Random(0)

while True:

    choice = input("Play a game? (Y/N): ")
    if choice == 'N':
        break

    target = dictionary[rng.randint(0, len(dictionary) - 1)]
    turns = 0
    MAX_TURNS = 6
    while True:
        if turns == MAX_TURNS:
            print("Game over! :(")
            print('The word was: {}'.format(target))
            break
        else:
            N=input(int())
            guessed=[]
            while len(guessed)<N:
                guess = input()
                guessed.append(guess)
                while not is_valid(guess, dictionary):
                    print('{} is not a valid word!'.format(guess))
                    guess = input()

                print("You guessed: {}".format(guess))
                response = compute_response(target, guess)
                print('Response: {}'.format(response))
                if response == guess:
                    # we won!
                    print("You win! :)")
                    break
            turns += 1

