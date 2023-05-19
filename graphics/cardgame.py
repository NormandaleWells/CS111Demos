#
# This shows one possible way of structuring a
# game that allows both human and computer
# players to be used interchangeably.
#
# The key is that as long as ComputerPlayer and
# HumanPlayer have the same methods (as shown
# here with the take_turn() method), they can
# be used interchangeably.

class ComputerPlayer:

    def __init__(self):
        pass

    def take_turn(self):
        pass

class HumanPlayer:

    def __init__(self):
        pass

    def take_turn(self):
        pass

class Game:

    # Note that Game does not know - or
    # care - whether player1 or player2
    # are actually human or computer
    # players.  We could even take an
    # arbitrary-sized list of players,
    # in which case run() would loop
    # through each player in the list
    # calling take_turn() for each one.
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def run(self):
        while True:
            self.player1.take_turn()
            self.player2.take_turn()

def main():
    # You could put up a rudimentary UI here
    # that allows the user to choose between
    # human and computer players for each of
    # any number of players.
    player1 = ComputerPlayer()
    player2 = HumanPlayer()
    game = Game(player1, player2)
    game.run()

if __name__ == "__main__":
    main()
