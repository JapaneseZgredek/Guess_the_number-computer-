import random


def guesser(x: int) -> bool:
    counter = 1
    picked_number = random.randint(0, x)

    while counter <= 10:
        guess: int = int(input(f'Attempt: {counter}. Input number that you want to guess: '))
        if guess == picked_number:
            return True
        if guess < picked_number:
            print("Your guess is lower than actual number")
        else:
            print("Your guess is greater than actual number")
        counter += 1

    return False


def main():
    x: int = int(input('Give me the top number: '))
    play: bool = True
    while play:
        if guesser(x):
            print('Yaaay you guessed the correct number in under 10 guesses')
        else:
            print('Unlucky, not this time bro.')
        user_play: str = ''
        while user_play != 'Y' and user_play != 'N':
            user_play: str = input('Play again ? Y/N.').upper()
            if user_play != 'Y' and user_play != 'N':
                print('Wrong input my man try again')
        if user_play == 'N':
            play = False


if __name__ == '__main__':
    main()
    print('Thank you for playing')

