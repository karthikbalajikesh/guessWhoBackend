'''
This file contains classes and methods that are related to every individual game
'''

from player import Player

class Game:
    def __init__(self, player1:Player, player2:Player, gameCode:str) -> None:
        self.player1 = player1
        self.player2 = player2
        self.gameCode = gameCode

        # will have to do random generation here
        self.getListOfCelebs()
        self.player1.setWhomToGuess(1)
        self.player2.setWhomToGuess(2)

    def getListOfCelebs(self) -> None:
        pass