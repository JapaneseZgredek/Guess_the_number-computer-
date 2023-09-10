import random
def guesser(x : int) -> bool:
    pass


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

