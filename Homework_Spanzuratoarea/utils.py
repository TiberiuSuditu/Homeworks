import random

list_of_countries = ['ROMANIA','CEHIA', 'ANGLIA', 'MAROC', 'FRANTA', 'CAMERUN', 'UCRAINA', 'POLONIA', 'GHANA']
country = random.choice(list_of_countries)
lives = 3
num_of_guesses = []
guessed = False

while not guessed:
    for word in country:
        if word.lower() in num_of_guesses:
            print(word, end=' ')
        else:
            print('_', end=' ')
    print('')

    guess = input(f'You have left {lives} tries, try again > ')
    num_of_guesses.append(guess.lower())
    if guess.lower() not in country.lower():
        lives -= 1
        if lives == 0:
            break

    guessed = True
    for word in country:
        if word.lower() not in num_of_guesses:
            guessed = False

if guessed:
    print(f'You won! The word was {country}!')

else:
    print(f'You lost! The word was {country}!')