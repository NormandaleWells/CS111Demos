'''
This is a simple guessing game.  The "game" selects a number from
0 to 10 (inclusive) and players try to guess the number.  Either
player may be either a human or a computer.

This may be useful as a general template for other two-player
games.
'''
import random

class Game:

    '''
    Initializaion just consists of generating a secret number.
    '''
    def __init__(self):
        self.number = random.randint(0, 10)

    '''
    Check to see if a given number is the secret number.
    '''
    def check_guess(self, guess):
        return guess == self.number

    '''
    run() - keep getting guesses until a player wins

    This shows the key point of this entire example; the Game
    class has no idea whether any given player is a human or
    a computer.  But since both the HumanPlayer and
    ComputerPlayer classes have a get_guess() method, this
    all Just Works, through the wonders of runtime polymorphism.
    '''    
    def run(self, player1, player2):
        while (True):
            guess = player1.get_guess()
            if self.check_guess(guess):
                return 1
            guess = player2.get_guess()
            if self.check_guess(guess):
                return 2


'''
A human player enters guesses via standard input.
'''
class HumanPlayer:

    '''
    We need to know our player number to display a meaningful prompt.
    '''
    def __init__(self, player_number):
        self.player_number = player_number

    '''
    Ask a human player for a guess.
    '''
    def get_guess(self):
        guess = int(input(f"What is your guess (player {self.player_number})? "))
        return guess
    

'''
A computer player just guesses randomly.
'''
class ComputerPlayer:

    '''
    Initialize the computer player by generating a list
    of all possible guesses, and then shuffling it.
    '''
    def __init__(self, player_number):
        self.player_number = player_number
        self.guess_list = [i for i in range(11)]
        random.shuffle(self.guess_list)
        self.next_guess = 0

    '''
    Return the next guess in the list of possible guesses.
    '''
    def get_guess(self):
        guess = self.guess_list[self.next_guess]
        print(f"The computer (player {self.player_number}) guesses {guess}")
        self.next_guess += 1
        return guess


'''
get_player() - ask whether the given player is a human or computer.
'''
def get_player(player_number):
    player_type = input(f"Is player {player_number} a computer or a person? (enter c or p): ")
    if player_type == "c":
        return ComputerPlayer(player_number)
    if player_type == "p":
        return HumanPlayer(player_number)
    return None


def main():
    game = Game()
    p1 = get_player(1)
    p2 = get_player(2)
    winner = game.run(p1, p2)
    print(f"Player {winner} wins!!!")


if __name__ == "__main__":
    main()
